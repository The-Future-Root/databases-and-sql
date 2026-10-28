# Solution to lesson 11: SQL from Python

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from run import fresh_database  # noqa: E402


def books_by_author(connection, author):
    """Return a list of the titles by this author, A to Z."""
    rows = connection.execute(
        "SELECT title FROM books WHERE author = ? ORDER BY title",
        (author,),
    ).fetchall()
    titles = []
    for row in rows:
        titles.append(row[0])
    return titles


def find_books(connection, text):
    """Return (title, price) pairs for books whose title contains text, in any case, A to Z."""
    return connection.execute(
        "SELECT title, price FROM books WHERE title LIKE '%' || ? || '%' ORDER BY title",
        (text,),
    ).fetchall()


def order_total(connection, order_id):
    """Return the total of an order, rounded to 2 places, or None if there's no such order."""
    row = connection.execute(
        "SELECT ROUND(SUM(quantity * unit_price), 2) FROM order_items WHERE order_id = ?",
        (order_id,),
    ).fetchone()
    return row[0]


def add_customer(connection, name, email, city, joined_on):
    """Add a customer, save the change, and return the new customer's id."""
    cursor = connection.execute(
        "INSERT INTO customers (name, email, city, joined_on) VALUES (?, ?, ?, ?)",
        (name, email, city, joined_on),
    )
    connection.commit()
    return cursor.lastrowid


def restock(connection, book_id, amount):
    """Add amount to a book's stock and save it. Raise ValueError if there's no such book."""
    cursor = connection.execute(
        "UPDATE books SET stock = stock + ? WHERE id = ?",
        (amount, book_id),
    )
    if cursor.rowcount == 0:
        raise ValueError(f"No book with id {book_id}")
    connection.commit()


if __name__ == "__main__":
    connection = fresh_database()
    print(books_by_author(connection, "Andy Weir"))
    print(find_books(connection, "night"))
    print(order_total(connection, 15))
    print(add_customer(connection, "Ella Brooks", "ella.brooks@example.com", "York", "2025-07-12"))
    restock(connection, 6, 12)
    print(connection.execute("SELECT title, stock FROM books WHERE id = 6").fetchone())
    print(books_by_author(connection, "x' OR '1'='1"))
