# Tests for this lesson. Run them from this folder with:  python3 -m unittest -v
# Each test runs your answer from exercise.sql on a fresh copy of the database.
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from sqltest import SqlLesson  # noqa: E402


class TestLesson(SqlLesson):
    empty = True
    cumulative = True

    def test_q1(self):
        self.check_after(1, 'SELECT name, "notnull", pk FROM pragma_table_info(\'members\') ORDER BY cid;', [('id', 0, 1), ('name', 1, 0), ('email', 1, 0)])

    def test_q1_refuses_1(self):
        self.check_rejects(1, "INSERT INTO members (name, email) VALUES ('A', 'same@example.com'); INSERT INTO members (name, email) VALUES ('B', 'same@example.com')", 'two members with the same email should be refused (UNIQUE)')

    def test_q1_refuses_2(self):
        self.check_rejects(1, "INSERT INTO members (email) VALUES ('x@example.com')", 'a member with no name should be refused')

    def test_q2(self):
        self.check_after(2, 'SELECT name, "notnull", pk FROM pragma_table_info(\'classes\') ORDER BY cid;', [('id', 0, 1), ('name', 1, 0), ('starts_at', 1, 0), ('capacity', 1, 0)])

    def test_q2_refuses_1(self):
        self.check_rejects(2, "INSERT INTO classes (name, starts_at, capacity) VALUES ('Spin', '2025-09-01 07:00', 0)", 'a class with a capacity of 0 should be refused (CHECK capacity > 0)')

    def test_q2_refuses_2(self):
        self.check_rejects(2, "INSERT INTO classes (name, capacity) VALUES ('Spin', 10)", 'a class with no start time should be refused')

    def test_q3(self):
        self.check_after(3, 'SELECT name, "notnull", pk FROM pragma_table_info(\'bookings\') ORDER BY cid;', [('member_id', 1, 1), ('class_id', 1, 2), ('booked_on', 1, 0)])

    def test_q3_refuses_1(self):
        self.check_rejects(3, "INSERT INTO members (id, name, email) VALUES (1, 'Nadia Hussain', 'nadia@example.com'), (2, 'Ben Carter', 'ben@example.com');\nINSERT INTO classes (id, name, starts_at, capacity) VALUES (1, 'Spin', '2025-09-01 07:00', 12), (2, 'Yoga', '2025-09-01 18:30', 20);\nINSERT INTO bookings (member_id, class_id, booked_on) VALUES (1, 1, '2025-08-28'), (2, 1, '2025-08-29'), (1, 2, '2025-08-30');\nINSERT INTO bookings (member_id, class_id, booked_on) VALUES (1, 1, '2025-08-31')", 'the same member booking the same class twice should be refused (PRIMARY KEY (member_id, class_id))')

    def test_q3_refuses_2(self):
        self.check_rejects(3, "INSERT INTO members (id, name, email) VALUES (1, 'Nadia Hussain', 'nadia@example.com'), (2, 'Ben Carter', 'ben@example.com');\nINSERT INTO classes (id, name, starts_at, capacity) VALUES (1, 'Spin', '2025-09-01 07:00', 12), (2, 'Yoga', '2025-09-01 18:30', 20);\nINSERT INTO bookings (member_id, class_id, booked_on) VALUES (1, 1, '2025-08-28'), (2, 1, '2025-08-29'), (1, 2, '2025-08-30');\nINSERT INTO bookings (member_id, class_id, booked_on) VALUES (9, 1, '2025-08-31')", "a booking for a member who doesn't exist should be refused (REFERENCES members(id))")

    def test_q3_refuses_3(self):
        self.check_rejects(3, "INSERT INTO members (id, name, email) VALUES (1, 'Nadia Hussain', 'nadia@example.com'), (2, 'Ben Carter', 'ben@example.com');\nINSERT INTO classes (id, name, starts_at, capacity) VALUES (1, 'Spin', '2025-09-01 07:00', 12), (2, 'Yoga', '2025-09-01 18:30', 20);\nINSERT INTO bookings (member_id, class_id, booked_on) VALUES (1, 1, '2025-08-28'), (2, 1, '2025-08-29'), (1, 2, '2025-08-30');\nINSERT INTO bookings (member_id, class_id, booked_on) VALUES (1, 9, '2025-08-31')", "a booking for a class that doesn't exist should be refused (REFERENCES classes(id))")

    def test_q3_accepts_1(self):
        self.check_accepts(3, "INSERT INTO members (id, name, email) VALUES (1, 'Nadia Hussain', 'nadia@example.com'), (2, 'Ben Carter', 'ben@example.com');\nINSERT INTO classes (id, name, starts_at, capacity) VALUES (1, 'Spin', '2025-09-01 07:00', 12), (2, 'Yoga', '2025-09-01 18:30', 20);\nINSERT INTO bookings (member_id, class_id, booked_on) VALUES (1, 1, '2025-08-28'), (2, 1, '2025-08-29'), (1, 2, '2025-08-30');", 'the example data in the README should go in without errors')

    def test_q4(self):
        self.check_query(4, [('Spin', 2), ('Yoga', 1)], ordered=True)


if __name__ == "__main__":
    unittest.main()
