"""Run a file of SQL against a fresh copy of the bookshop database and print the results.

    python3 run.py 02-selecting-data/exercise.sql      run every statement in the file
    python3 run.py -c "SELECT title FROM books;"        run one query
    python3 run.py --empty 04-creating-tables/exercise.sql   start from an empty database instead
    python3 run.py --save bookshop.db                   write the database to a file you can open in other tools

Every run starts again from data/bookshop.sql, so you can't break anything.
"""
import argparse
import pathlib
import sqlite3
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data" / "bookshop.sql"


def fresh_database(empty=False):
    """Return a connection to a new in-memory database, filled with the bookshop data unless empty is True."""
    connection = sqlite3.connect(":memory:", isolation_level=None)
    connection.execute("PRAGMA foreign_keys = ON")
    if not empty:
        connection.executescript(DATA.read_text())
    return connection


def show(cursor, rows):
    """Print rows as a table with a header line."""
    headers = [column[0] for column in cursor.description]
    text = [["NULL" if value is None else str(value) for value in row] for row in rows]
    widths = [len(h) for h in headers]
    for row in text:
        for i, value in enumerate(row):
            widths[i] = max(widths[i], len(value))
    print("  ".join(h.ljust(w) for h, w in zip(headers, widths)).rstrip())
    print("  ".join("-" * w for w in widths))
    for row in text:
        print("  ".join(v.ljust(w) for v, w in zip(row, widths)).rstrip())
    print(f"({len(rows)} row{'s' if len(rows) != 1 else ''})\n")


def statements(sql):
    """Split SQL text into complete statements, ignoring comment-only leftovers."""
    current = ""
    for character in sql:
        current += character
        if character == ";" and sqlite3.complete_statement(current):
            yield current.strip()
            current = ""
    if strip_comments(current):
        yield current.strip()


def strip_comments(statement):
    """Return the statement without its -- comment lines."""
    return "\n".join(line for line in statement.splitlines() if not line.strip().startswith("--")).strip()


def run(connection, sql):
    """Run each statement, printing results of queries and the number of rows other statements changed."""
    for statement in statements(sql):
        code = strip_comments(statement)
        if not code:
            continue
        print("sql> " + code.replace("\n", "\n...  "))
        try:
            cursor = connection.execute(code)
        except sqlite3.Error as error:
            print(f"Error: {error}\n")
            continue
        if cursor.description:
            show(cursor, cursor.fetchall())
        else:
            changed = cursor.rowcount
            if changed >= 0:
                print(f"OK, {changed} row{'s' if changed != 1 else ''} changed\n")
            else:
                print("OK\n")
    connection.commit()


def main():
    parser = argparse.ArgumentParser(description="Run SQL against a fresh copy of the bookshop database.")
    parser.add_argument("file", nargs="?", help="a .sql file to run")
    parser.add_argument("-c", "--command", help="SQL to run, instead of a file")
    parser.add_argument("--empty", action="store_true", help="start from an empty database")
    parser.add_argument("--save", metavar="PATH", help="also write the database to this file")
    args = parser.parse_args()
    connection = fresh_database(args.empty)
    if args.command:
        run(connection, args.command)
    elif args.file:
        run(connection, pathlib.Path(args.file).read_text())
    elif not args.save:
        parser.print_help()
        return 1
    if args.save:
        target = sqlite3.connect(args.save)
        connection.backup(target)
        target.close()
        print(f"Saved the database to {args.save}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
