# Lesson 11: SQL from Python
#
# Always pass values with ? placeholders. Never build SQL with f-strings, + or .format().
# Test with:  python3 -m unittest -v

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from run import fresh_database  # noqa: E402


def books_by_author(connection, author):
    """Return a list of the titles by this author, A to Z."""
    pass


def find_books(connection, text):
    """Return (title, price) pairs for books whose title contains text, in any case, A to Z."""
    pass


def order_total(connection, order_id):
    """Return the total of an order, rounded to 2 places, or None if there's no such order."""
    pass


def add_customer(connection, name, email, city, joined_on):
    """Add a customer, save the change, and return the new customer's id."""
    pass


def restock(connection, book_id, amount):
    """Add amount to a book's stock and save it. Raise ValueError if there's no such book."""
    pass


if __name__ == "__main__":
    connection = fresh_database()
    print(books_by_author(connection, "Andy Weir"))
    print(find_books(connection, "night"))
    print(order_total(connection, 15))
    print(add_customer(connection, "Ella Brooks", "ella.brooks@example.com", "York", "2025-07-12"))
    restock(connection, 6, 12)
    print(connection.execute("SELECT title, stock FROM books WHERE id = 6").fetchone())
    print(books_by_author(connection, "x' OR '1'='1"))
