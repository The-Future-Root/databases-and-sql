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
        self.check_after(1, 'SELECT id, price FROM books ORDER BY id;', [(1, 9.99), (2, 11.49), (3, 6.99), (4, 9.49), (5, 12.99), (6, 14.99), (7, 8.99), (8, 8.49), (9, 7.99), (10, 11.99), (11, 10.99), (12, 10.49), (13, 9.99), (14, 5.99), (15, 11.49), (16, 10.49), (17, 12.49), (18, 9.99), (19, 9.49), (20, 13.49)])

    def test_q2(self):
        self.check_after(2, 'SELECT id, status FROM orders ORDER BY id;', [(1, 'delivered'), (2, 'delivered'), (3, 'delivered'), (4, 'delivered'), (5, 'delivered'), (6, 'delivered'), (7, 'cancelled'), (8, 'delivered'), (9, 'delivered'), (10, 'delivered'), (11, 'delivered'), (12, 'delivered'), (13, 'delivered'), (14, 'delivered'), (15, 'delivered'), (16, 'delivered'), (17, 'delivered'), (18, 'delivered'), (19, 'cancelled'), (20, 'shipped'), (21, 'shipped'), (22, 'shipped'), (23, 'shipped'), (24, 'delivered'), (25, 'delivered'), (26, 'delivered')])

    def test_q3(self):
        self.check_after(3, 'SELECT id, stock FROM books ORDER BY id;', [(1, 14), (2, 8), (3, 20), (4, 5), (5, 11), (6, 10), (7, 6), (8, 3), (9, 17), (10, 9), (11, 7), (12, 4), (13, 12), (14, 10), (15, 2), (16, 10), (17, 6), (18, 8), (19, 15), (20, 5)])

    def test_q4(self):
        self.check_after(4, 'SELECT id, price FROM books ORDER BY id;', [(1, 9.99), (2, 11.49), (3, 6.29), (4, 9.49), (5, 12.99), (6, 14.99), (7, 8.99), (8, 8.49), (9, 7.19), (10, 11.99), (11, 10.99), (12, 10.49), (13, 9.99), (14, 5.39), (15, 11.49), (16, 10.49), (17, 12.49), (18, 9.99), (19, 9.49), (20, 13.49)])

    def test_q5(self):
        self.check_after(5, "SELECT (SELECT COUNT(*) FROM orders), (SELECT COUNT(*) FROM order_items), (SELECT COUNT(*) FROM orders WHERE status = 'cancelled'), (SELECT COUNT(*) FROM order_items WHERE order_id NOT IN (SELECT id FROM orders));", [(24, 42, 0, 0)])

    def test_q6(self):
        self.check_after(6, 'SELECT id, phone FROM customers ORDER BY id;', [(1, '0113 496 0000'), (2, None), (3, None), (4, None), (5, None), (6, None), (7, None), (8, None), (9, None), (10, None), (11, None), (12, None)])


if __name__ == "__main__":
    unittest.main()
