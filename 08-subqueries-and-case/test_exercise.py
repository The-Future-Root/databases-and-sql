# Tests for this lesson. Run them from this folder with:  python3 -m unittest -v
# Each test runs your answer from exercise.sql on a fresh copy of the database.
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from sqltest import SqlLesson  # noqa: E402


class TestLesson(SqlLesson):
    def test_q1(self):
        self.check_query(1, [('Atomic Habits', 14.99), ('Thinking, Fast and Slow', 13.49), ('Sapiens', 12.99), ('Klara and the Sun', 12.49), ('Project Hail Mary', 11.99), ('A Brief History of Time', 11.49), ('Dune', 10.99), ('The Fellowship of the Ring', 10.99), ('Educated', 10.49), ('The Name of the Wind', 10.49)], ordered=True)
        self.check_uses(1, '\\(\\s*SELECT', 'use a subquery to work out the average')

    def test_q2(self):
        self.check_query(2, [('Aisha Bello',), ('Daniel Okafor',), ('Lucas Moreau',), ('Mei Lin',), ('Omar Haddad',), ('Priya Shah',), ('Sofia Rossi',), ('Tom Becker',)], ordered=True)
        self.check_uses(2, '\\bIN\\s*\\(\\s*SELECT', 'use IN (SELECT ...)')

    def test_q3(self):
        self.check_query(3, [('Frankenstein', 5.99, 'budget'), ('Pride and Prejudice', 6.99, 'budget'), ('Nineteen Eighty-Four', 7.99, 'budget'), ('Gone Girl', 8.49, 'standard'), ('The Girl with the Dragon Tattoo', 8.99, 'standard'), ('The Martian', 9.49, 'standard'), ('The Midnight Library', 9.49, 'standard'), ('Normal People', 9.99, 'standard'), ('The Hobbit', 9.99, 'standard'), ('The Thursday Murder Club', 9.99, 'standard'), ('Educated', 10.49, 'standard'), ('The Name of the Wind', 10.49, 'standard'), ('Dune', 10.99, 'standard'), ('The Fellowship of the Ring', 10.99, 'standard'), ('A Brief History of Time', 11.49, 'standard'), ('Project Hail Mary', 11.99, 'standard'), ('Klara and the Sun', 12.49, 'premium'), ('Sapiens', 12.99, 'premium'), ('Thinking, Fast and Slow', 13.49, 'premium'), ('Atomic Habits', 14.99, 'premium')], ordered=True, names=['title', 'price', 'band'])

    def test_q4(self):
        self.check_query(4, [('fine', 15), ('low', 3), ('out of stock', 2)], ordered=True)

    def test_q5(self):
        self.check_query(5, [(30.7,)])
        self.check_uses(5, '^\\s*WITH\\b', 'start with WITH order_totals AS (...)')

    def test_q6(self):
        self.check_query(6, [('Sofia Rossi', '2025-07-10')])


if __name__ == "__main__":
    unittest.main()
