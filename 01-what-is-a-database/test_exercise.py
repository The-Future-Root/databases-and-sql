# Tests for this lesson. Run them from this folder with:  python3 -m unittest -v
# Each test runs your answer from exercise.sql on a fresh copy of the database.
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from sqltest import SqlLesson  # noqa: E402


class TestLesson(SqlLesson):
    def test_q1(self):
        self.check_query(1, [(1, 'Priya Shah', 'priya.shah@example.com', 'Leeds', '2024-02-11'), (2, 'Tom Becker', 'tom.becker@example.com', 'Manchester', '2024-03-02'), (3, 'Aisha Bello', 'aisha.bello@example.com', 'London', '2024-03-19'), (4, 'Daniel Okafor', 'daniel.okafor@example.com', 'Leeds', '2024-05-07'), (5, 'Mei Lin', 'mei.lin@example.com', 'Bristol', '2024-06-23'), (6, 'Lucas Moreau', 'lucas.moreau@example.com', 'London', '2024-08-14'), (7, 'Hannah Fischer', 'hannah.fischer@example.com', None, '2024-09-01'), (8, 'Omar Haddad', 'omar.haddad@example.com', 'Manchester', '2024-11-30'), (9, 'Sofia Rossi', 'sofia.rossi@example.com', 'Bristol', '2025-01-08'), (10, 'Jack Wilson', 'jack.wilson@example.com', 'London', '2025-02-17'), (11, 'Grace Kim', 'grace.kim@example.com', 'Leeds', '2025-03-05'), (12, 'Ravi Patel', 'ravi.patel@example.com', 'Glasgow', '2025-03-28')])

    def test_q2(self):
        self.check_query(2, [('The Hobbit', 'J.R.R. Tolkien'), ('Dune', 'Frank Herbert'), ('Pride and Prejudice', 'Jane Austen'), ('The Martian', 'Andy Weir'), ('Sapiens', 'Yuval Noah Harari'), ('Atomic Habits', 'James Clear'), ('The Girl with the Dragon Tattoo', 'Stieg Larsson'), ('Gone Girl', 'Gillian Flynn'), ('Nineteen Eighty-Four', 'George Orwell'), ('Project Hail Mary', 'Andy Weir'), ('The Fellowship of the Ring', 'J.R.R. Tolkien'), ('Educated', 'Tara Westover'), ('The Thursday Murder Club', 'Richard Osman'), ('Frankenstein', 'Mary Shelley'), ('A Brief History of Time', 'Stephen Hawking'), ('The Name of the Wind', 'Patrick Rothfuss'), ('Klara and the Sun', 'Kazuo Ishiguro'), ('Normal People', 'Sally Rooney'), ('The Midnight Library', 'Matt Haig'), ('Thinking, Fast and Slow', 'Daniel Kahneman')])

    def test_q3(self):
        self.check_query(3, [(1, 1, 'delivered'), (2, 6, 'delivered'), (3, 1, 'delivered'), (4, 1, 'delivered'), (5, 8, 'delivered'), (6, 3, 'delivered'), (7, 1, 'cancelled'), (8, 6, 'delivered'), (9, 1, 'delivered'), (10, 4, 'delivered'), (11, 9, 'delivered'), (12, 3, 'delivered'), (13, 3, 'delivered'), (14, 2, 'delivered'), (15, 3, 'delivered'), (16, 3, 'delivered'), (17, 2, 'delivered'), (18, 1, 'delivered'), (19, 3, 'cancelled'), (20, 8, 'shipped'), (21, 6, 'shipped'), (22, 5, 'shipped'), (23, 6, 'pending'), (24, 3, 'delivered'), (25, 5, 'delivered'), (26, 9, 'delivered')])


if __name__ == "__main__":
    unittest.main()
