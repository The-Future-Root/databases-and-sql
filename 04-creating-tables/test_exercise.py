# Tests for this lesson. Run them from this folder with:  python3 -m unittest -v
# Each test runs your answer from exercise.sql on a fresh copy of the database.
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from sqltest import SqlLesson  # noqa: E402


class TestLesson(SqlLesson):
    cumulative = True

    def test_q1(self):
        self.check_after(1, 'SELECT name, type, "notnull", pk FROM pragma_table_info(\'reviews\') ORDER BY cid;', [('id', 'INTEGER', 0, 1), ('book_id', 'INTEGER', 1, 0), ('customer_id', 'INTEGER', 1, 0), ('rating', 'INTEGER', 1, 0), ('comment', 'TEXT', 0, 0), ('reviewed_on', 'TEXT', 1, 0)])

    def test_q1_refuses_1(self):
        self.check_rejects(1, "INSERT INTO reviews (book_id, customer_id, rating, reviewed_on) VALUES (1, 1, 6, '2025-07-01')", 'a rating of 6 should be refused (CHECK rating BETWEEN 1 AND 5)')

    def test_q1_refuses_2(self):
        self.check_rejects(1, "INSERT INTO reviews (book_id, customer_id, rating, reviewed_on) VALUES (1, 1, 0, '2025-07-01')", 'a rating of 0 should be refused')

    def test_q1_refuses_3(self):
        self.check_rejects(1, "INSERT INTO reviews (book_id, customer_id, reviewed_on) VALUES (1, 1, '2025-07-01')", 'a review with no rating should be refused (NOT NULL)')

    def test_q1_refuses_4(self):
        self.check_rejects(1, 'INSERT INTO reviews (book_id, customer_id, rating) VALUES (1, 1, 4)', 'a review with no reviewed_on date should be refused')

    def test_q1_refuses_5(self):
        self.check_rejects(1, "INSERT INTO reviews (book_id, customer_id, rating, reviewed_on) VALUES (999, 1, 4, '2025-07-01')", "a review of a book that doesn't exist should be refused (REFERENCES books(id))")

    def test_q1_refuses_6(self):
        self.check_rejects(1, "INSERT INTO reviews (book_id, customer_id, rating, reviewed_on) VALUES (1, 999, 4, '2025-07-01')", "a review by a customer who doesn't exist should be refused (REFERENCES customers(id))")

    def test_q1_accepts_1(self):
        self.check_accepts(1, "INSERT INTO reviews (book_id, customer_id, rating, reviewed_on) VALUES (1, 1, 5, '2025-07-01')", 'a review with just the required columns should work')

    def test_q2(self):
        self.check_after(2, 'SELECT id, book_id, customer_id, rating, comment, reviewed_on FROM reviews ORDER BY id;', [(1, 5, 1, 5, 'Changed how I think about history.', '2025-04-20'), (2, 19, 3, 4, 'A lovely, gentle read.', '2025-06-02'), (3, 8, 6, 3, None, '2025-06-14')])

    def test_q3(self):
        self.check_after(3, 'SELECT * FROM books WHERE id > 20;', [(21, 'Tomorrow, and Tomorrow, and Tomorrow', 'Gabrielle Zevin', 'Fiction', 10.99, 6, 2022)])

    def test_q4(self):
        self.check_after(4, 'SELECT * FROM customers WHERE id > 12;', [(13, 'Ella Brooks', 'ella.brooks@example.com', 'York', '2025-07-12')])


if __name__ == "__main__":
    unittest.main()
