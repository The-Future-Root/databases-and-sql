import ast
import pathlib
import sqlite3
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from run import fresh_database  # noqa: E402
from exercise import add_customer, books_by_author, find_books, order_total, restock  # noqa: E402

SOURCE = pathlib.Path(__file__).with_name("exercise.py").read_text()
SNEAKY = "x' OR '1'='1"


class TestBooksByAuthor(unittest.TestCase):
    def setUp(self):
        self.db = fresh_database()

    def test_titles(self):
        self.assertEqual(books_by_author(self.db, "Andy Weir"), ["Project Hail Mary", "The Martian"])
        self.assertEqual(books_by_author(self.db, "Jane Austen"), ["Pride and Prejudice"])

    def test_plain_strings(self):
        titles = books_by_author(self.db, "J.R.R. Tolkien")
        self.assertEqual(titles, ["The Fellowship of the Ring", "The Hobbit"])
        self.assertIsInstance(titles[0], str, "Return the titles themselves, not rows like ('The Hobbit',)")

    def test_nobody(self):
        self.assertEqual(books_by_author(self.db, "Nobody"), [])

    def test_injection(self):
        self.assertEqual(books_by_author(self.db, SNEAKY), [], "A name with quotes in it must be treated as plain text: use a ? placeholder")


class TestFindBooks(unittest.TestCase):
    def setUp(self):
        self.db = fresh_database()

    def test_find(self):
        self.assertEqual(find_books(self.db, "night"), [("The Midnight Library", 9.49)])
        self.assertEqual(find_books(self.db, "THE M"), [("The Martian", 9.49), ("The Midnight Library", 9.49)], "Any case, A to Z")

    def test_nothing(self):
        self.assertEqual(find_books(self.db, "zebra"), [])

    def test_injection(self):
        self.assertEqual(find_books(self.db, SNEAKY), [])


class TestOrderTotal(unittest.TestCase):
    def setUp(self):
        self.db = fresh_database()

    def test_totals(self):
        self.assertEqual(order_total(self.db, 15), 71.44)
        self.assertEqual(order_total(self.db, 3), 9.99)

    def test_missing(self):
        self.assertIsNone(order_total(self.db, 999))


class TestAddCustomer(unittest.TestCase):
    def setUp(self):
        self.db = fresh_database()

    def test_adds_and_returns_id(self):
        new_id = add_customer(self.db, "Ella Brooks", "ella.brooks@example.com", "York", "2025-07-12")
        self.assertEqual(new_id, 13)
        row = self.db.execute("SELECT name, email, city, joined_on FROM customers WHERE id = ?", (new_id,)).fetchone()
        self.assertEqual(row, ("Ella Brooks", "ella.brooks@example.com", "York", "2025-07-12"))

    def test_awkward_name(self):
        new_id = add_customer(self.db, "Siobhán O'Neill", "siobhan@example.com", None, "2025-07-13")
        name, city = self.db.execute("SELECT name, city FROM customers WHERE id = ?", (new_id,)).fetchone()
        self.assertEqual(name, "Siobhán O'Neill", "An apostrophe in a name must just work")
        self.assertIsNone(city, "Passing None should store NULL")

    def test_duplicate_email(self):
        with self.assertRaises(sqlite3.IntegrityError):
            add_customer(self.db, "Copy", "priya.shah@example.com", "Leeds", "2025-07-13")


class TestRestock(unittest.TestCase):
    def setUp(self):
        self.db = fresh_database()

    def test_restock(self):
        restock(self.db, 6, 12)
        self.assertEqual(self.db.execute("SELECT stock FROM books WHERE id = 6").fetchone(), (12,))
        restock(self.db, 6, 3)
        self.assertEqual(self.db.execute("SELECT stock FROM books WHERE id = 6").fetchone(), (15,))

    def test_missing_book(self):
        with self.assertRaises(ValueError):
            restock(self.db, 999, 5)


class TestPlaceholders(unittest.TestCase):
    def test_sql_is_never_built_from_pieces(self):
        for node in ast.walk(ast.parse(SOURCE)):
            if isinstance(node, ast.Call) and getattr(node.func, "attr", None) == "execute" and node.args:
                self.assertIsInstance(node.args[0], ast.Constant, "Pass execute() a plain string with ? placeholders, and the values separately. Don't build SQL with f-strings, + or .format()")


if __name__ == "__main__":
    unittest.main()
