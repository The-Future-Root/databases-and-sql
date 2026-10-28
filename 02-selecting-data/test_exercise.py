# Tests for this lesson. Run them from this folder with:  python3 -m unittest -v
# Each test runs your answer from exercise.sql on a fresh copy of the database.
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from sqltest import SqlLesson  # noqa: E402


class TestLesson(SqlLesson):
    def test_q1(self):
        self.check_query(1, [('Atomic Habits', 14.99), ('Thinking, Fast and Slow', 13.49), ('Sapiens', 12.99), ('Klara and the Sun', 12.49), ('Project Hail Mary', 11.99), ('A Brief History of Time', 11.49), ('Dune', 10.99), ('The Fellowship of the Ring', 10.99), ('Educated', 10.49), ('The Name of the Wind', 10.49), ('Normal People', 9.99), ('The Hobbit', 9.99), ('The Thursday Murder Club', 9.99), ('The Martian', 9.49), ('The Midnight Library', 9.49), ('The Girl with the Dragon Tattoo', 8.99), ('Gone Girl', 8.49), ('Nineteen Eighty-Four', 7.99), ('Pride and Prejudice', 6.99), ('Frankenstein', 5.99)], ordered=True)

    def test_q2(self):
        self.check_query(2, [('Frankenstein', 5.99), ('Pride and Prejudice', 6.99), ('Nineteen Eighty-Four', 7.99), ('Gone Girl', 8.49), ('The Girl with the Dragon Tattoo', 8.99)], ordered=True)

    def test_q3(self):
        self.check_query(3, [('Classics',), ('Crime',), ('Fantasy',), ('Fiction',), ('Non-fiction',), ('Science Fiction',)], ordered=True)

    def test_q4(self):
        self.check_query(4, [('Sapiens', 142.89), ('The Midnight Library', 142.35), ('The Hobbit', 139.86), ('Pride and Prejudice', 139.8), ('Nineteen Eighty-Four', 135.83), ('The Thursday Murder Club', 119.88), ('Project Hail Mary', 107.91), ('Dune', 87.92), ('Normal People', 79.92), ('The Fellowship of the Ring', 76.93), ('Klara and the Sun', 74.94), ('Thinking, Fast and Slow', 67.45), ('Frankenstein', 59.9), ('The Girl with the Dragon Tattoo', 53.94), ('The Martian', 47.45), ('Educated', 41.96), ('Gone Girl', 25.47), ('A Brief History of Time', 22.98), ('Atomic Habits', 0.0), ('The Name of the Wind', 0.0)], ordered=True, names=['title', 'stock_value'])

    def test_q5(self):
        self.check_query(5, [('Ravi Patel', '2025-03-28'), ('Grace Kim', '2025-03-05'), ('Jack Wilson', '2025-02-17')], ordered=True)

    def test_q6(self):
        self.check_query(6, [(None,), ('Bristol',), ('Glasgow',), ('Leeds',), ('London',), ('Manchester',)], ordered=True)


if __name__ == "__main__":
    unittest.main()
