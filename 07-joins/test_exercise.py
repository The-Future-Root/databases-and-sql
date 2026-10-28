# Tests for this lesson. Run them from this folder with:  python3 -m unittest -v
# Each test runs your answer from exercise.sql on a fresh copy of the database.
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from sqltest import SqlLesson  # noqa: E402


class TestLesson(SqlLesson):
    def test_q1(self):
        self.check_query(1, [(1, 'Priya Shah', '2025-04-06'), (2, 'Lucas Moreau', '2025-04-10'), (3, 'Priya Shah', '2025-04-11'), (4, 'Priya Shah', '2025-04-15'), (5, 'Omar Haddad', '2025-04-16'), (6, 'Aisha Bello', '2025-04-22'), (7, 'Priya Shah', '2025-04-27'), (8, 'Lucas Moreau', '2025-04-29'), (9, 'Priya Shah', '2025-05-02'), (10, 'Daniel Okafor', '2025-05-07'), (11, 'Sofia Rossi', '2025-05-13'), (12, 'Aisha Bello', '2025-05-21'), (13, 'Aisha Bello', '2025-05-26'), (14, 'Tom Becker', '2025-05-31'), (15, 'Aisha Bello', '2025-06-01'), (16, 'Aisha Bello', '2025-06-06'), (17, 'Tom Becker', '2025-06-08'), (18, 'Priya Shah', '2025-06-09'), (19, 'Aisha Bello', '2025-06-15'), (20, 'Omar Haddad', '2025-06-20'), (21, 'Lucas Moreau', '2025-06-22'), (22, 'Mei Lin', '2025-06-25'), (23, 'Lucas Moreau', '2025-06-29'), (24, 'Aisha Bello', '2025-07-01'), (25, 'Mei Lin', '2025-07-07'), (26, 'Sofia Rossi', '2025-07-10')], ordered=True)
        self.check_uses(1, '\\bJOIN\\b', 'use JOIN')

    def test_q2(self):
        self.check_query(2, [('The Thursday Murder Club', 1, 9.99)], ordered=True)

    def test_q3(self):
        self.check_query(3, [('Aisha Bello', 7), ('Priya Shah', 6), ('Lucas Moreau', 4), ('Mei Lin', 2), ('Omar Haddad', 2), ('Sofia Rossi', 2), ('Tom Becker', 2), ('Daniel Okafor', 1), ('Grace Kim', 0), ('Hannah Fischer', 0), ('Jack Wilson', 0), ('Ravi Patel', 0)], ordered=True)
        self.check_uses(3, 'LEFT\\s+(OUTER\\s+)?JOIN', 'use LEFT JOIN so customers with no orders still appear')

    def test_q4(self):
        self.check_query(4, [('Dune',), ('Frankenstein',), ('Klara and the Sun',)])

    def test_q5(self):
        self.check_query(5, [('Aisha Bello', 225.09), ('Priya Shah', 133.37), ('Tom Becker', 86.92), ('Lucas Moreau', 58.95), ('Sofia Rossi', 46.46), ('Daniel Okafor', 40.95), ('Mei Lin', 14.99), ('Omar Haddad', 7.19)], ordered=True)

    def test_q6(self):
        self.check_query(6, [('Non-fiction', 25), ('Fiction', 13), ('Crime', 11), ('Fantasy', 11), ('Classics', 10), ('Science Fiction', 2)], ordered=True)


if __name__ == "__main__":
    unittest.main()
