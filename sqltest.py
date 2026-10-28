"""Helpers for the lesson tests. You don't need to read this to do the exercises.

An exercise.sql file holds answers under markers like:

    -- Q1: Every book's title.
    SELECT title FROM books;

Each test runs answers on a fresh copy of the bookshop database and compares the results.
"""
import pathlib
import re
import sqlite3
import unittest

from run import fresh_database, statements, strip_comments

MARKER = re.compile(r"^--\s*Q(\d+):", re.MULTILINE)


def read_answers(path):
    """Return {question number: SQL text} from an exercise file."""
    text = pathlib.Path(path).read_text()
    marks = list(MARKER.finditer(text))
    answers = {}
    for i, mark in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        answers[int(mark.group(1))] = strip_comments(text[mark.end():end].split("\n", 1)[1] if "\n" in text[mark.end():end] else "")
    return answers


def tidy(rows):
    """Round floats so 51.970000000000006 and 51.97 count as the same answer."""
    return [tuple(round(v, 2) if isinstance(v, float) else v for v in row) for row in rows]


class SqlLesson(unittest.TestCase):
    """Base class for a lesson's tests."""

    empty = False
    cumulative = False
    exercise = "exercise.sql"

    @classmethod
    def setUpClass(cls):
        folder = pathlib.Path(__import__(cls.__module__).__file__).resolve().parent
        cls.answers = read_answers(folder / cls.exercise)

    def answer(self, number):
        sql = self.answers.get(number, "")
        if not sql:
            self.fail(f"Q{number} isn't answered yet: write your SQL under the '-- Q{number}:' line")
        return sql

    def execute(self, connection, number):
        """Run every statement of an answer and return the cursor of the last one."""
        cursor = None
        for statement in statements(self.answer(number)):
            code = strip_comments(statement)
            if not code:
                continue
            try:
                cursor = connection.execute(code)
            except sqlite3.Error as error:
                self.fail(f"Q{number} gives an error: {error}")
        return cursor

    def check_query(self, number, expected, ordered=False, names=None):
        """The answer's last statement must be a query returning exactly these rows."""
        connection = self.after_answers(number - 1) if self.cumulative else fresh_database(self.empty)
        cursor = self.execute(connection, number)
        if cursor is None or cursor.description is None:
            self.fail(f"Q{number} should end with a SELECT query")
        rows = tidy(cursor.fetchall())
        columns = [column[0] for column in cursor.description]
        expected = tidy(expected)
        if expected and len(columns) != len(expected[0]):
            self.fail(f"Q{number} should return {len(expected[0])} column(s), but yours returns {len(columns)}: {columns}")
        if names is not None:
            self.assertEqual([c.lower() for c in columns], [n.lower() for n in names], f"Q{number}: name the columns {names} (use AS)")
        if ordered:
            self.assertEqual(rows, expected, f"Q{number}: the rows, or their order, aren't right")
        else:
            self.assertCountEqual(rows, expected, f"Q{number}: the rows aren't right")

    def check_after(self, number, check, expected, ordered=True):
        """Run answers 1 to number in order, then this check query must return the expected rows."""
        connection = self.after_answers(number)
        rows = tidy(connection.execute(check).fetchall())
        message = f"Q{number}: after your SQL, the data isn't right"
        if number > 1:
            message += f". The answers run in order, so check Q1 to Q{number - 1} too"
        if ordered:
            self.assertEqual(rows, tidy(expected), message)
        else:
            self.assertCountEqual(rows, tidy(expected), message)

    def check_uses(self, number, pattern, message):
        """The answer must contain a pattern, like GROUP BY or LEFT JOIN."""
        if not re.search(pattern, self.answer(number), re.IGNORECASE):
            self.fail(f"Q{number}: {message}")

    def after_answers(self, number):
        """Return a fresh database with answers 1 to number run in order."""
        connection = fresh_database(self.empty)
        for n in range(1, number + 1):
            self.execute(connection, n)
        return connection

    def check_rejects(self, number, sql, message):
        """After answers 1 to number, this SQL must fail (for example, because of a constraint)."""
        connection = self.after_answers(number)
        try:
            connection.executescript(sql)
        except sqlite3.Error:
            return
        self.fail(f"Q{number}: {message}")

    def check_accepts(self, number, sql, message):
        """After answers 1 to number, this SQL must work."""
        connection = self.after_answers(number)
        try:
            connection.executescript(sql)
        except sqlite3.Error as error:
            self.fail(f"Q{number}: {message}, but it gave an error: {error}")
