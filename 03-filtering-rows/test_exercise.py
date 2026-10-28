# Tests for this lesson. Run them from this folder with:  python3 -m unittest -v
# Each test runs your answer from exercise.sql on a fresh copy of the database.
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from sqltest import SqlLesson  # noqa: E402


class TestLesson(SqlLesson):
    def test_q1(self):
        self.check_query(1, [('The Girl with the Dragon Tattoo', 8.99), ('Gone Girl', 8.49), ('The Thursday Murder Club', 9.99)])

    def test_q2(self):
        self.check_query(2, [('Frankenstein', 5.99), ('Pride and Prejudice', 6.99), ('Nineteen Eighty-Four', 7.99), ('Gone Girl', 8.49), ('The Girl with the Dragon Tattoo', 8.99), ('The Martian', 9.49), ('The Midnight Library', 9.49)], ordered=True)

    def test_q3(self):
        self.check_query(3, [('The Hobbit', 'Fantasy'), ('Dune', 'Science Fiction'), ('The Martian', 'Science Fiction'), ('Project Hail Mary', 'Science Fiction'), ('The Fellowship of the Ring', 'Fantasy')])
        self.check_uses(3, '\\bIN\\s*\\(', "use IN ('Fantasy', 'Science Fiction')")

    def test_q4(self):
        self.check_query(4, [('Sapiens', 2011), ('The Martian', 2011), ('Thinking, Fast and Slow', 2011), ('Gone Girl', 2012), ('Atomic Habits', 2018), ('Educated', 2018), ('Normal People', 2018)], ordered=True)
        self.check_uses(4, '\\bBETWEEN\\b', 'use BETWEEN')

    def test_q5(self):
        self.check_query(5, [('The Hobbit',), ('The Martian',), ('The Girl with the Dragon Tattoo',), ('The Fellowship of the Ring',), ('The Thursday Murder Club',), ('The Name of the Wind',), ('Klara and the Sun',), ('The Midnight Library',)])
        self.check_uses(5, '\\bLIKE\\b', 'use LIKE')

    def test_q6(self):
        self.check_query(6, [('Hannah Fischer', 'hannah.fischer@example.com')])
        self.check_uses(6, '\\bIS\\s+NULL\\b', 'use IS NULL (= NULL never matches anything)')

    def test_q7(self):
        self.check_query(7, [(20, 'shipped'), (21, 'shipped'), (22, 'shipped'), (23, 'pending')])


if __name__ == "__main__":
    unittest.main()
