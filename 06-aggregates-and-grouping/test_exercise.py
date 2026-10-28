# Tests for this lesson. Run them from this folder with:  python3 -m unittest -v
# Each test runs your answer from exercise.sql on a fresh copy of the database.
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from sqltest import SqlLesson  # noqa: E402


class TestLesson(SqlLesson):
    def test_q1(self):
        self.check_query(1, [(20,)], names=['book_count'])

    def test_q2(self):
        self.check_query(2, [(162, 10.39, 5.99, 14.99)])

    def test_q3(self):
        self.check_query(3, [('Classics', 3, 6.99), ('Crime', 3, 9.16), ('Fantasy', 3, 10.49), ('Fiction', 3, 10.66), ('Non-fiction', 5, 12.69), ('Science Fiction', 3, 10.82)], ordered=True)
        self.check_uses(3, 'GROUP\\s+BY', 'use GROUP BY')

    def test_q4(self):
        self.check_query(4, [(15, 71.44), (17, 53.46), (9, 47.95), (22, 45.96), (21, 44.95)], ordered=True, names=['order_id', 'total'])

    def test_q5(self):
        self.check_query(5, [('Bristol', 2), ('Leeds', 3), ('London', 3), ('Manchester', 2)], ordered=True)
        self.check_uses(5, '\\bHAVING\\b', 'use HAVING')

    def test_q6(self):
        self.check_query(6, [('2025-04', 8), ('2025-05', 6), ('2025-06', 9), ('2025-07', 3)], ordered=True, names=['month', 'orders'])


if __name__ == "__main__":
    unittest.main()
