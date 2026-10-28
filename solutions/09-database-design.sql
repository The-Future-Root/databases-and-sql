-- Lesson 9: designing tables for a gym
--
-- Write each answer under its question. Run them all with:
--     python3 ../run.py --empty exercise.sql
-- and check them with:
--     python3 -m unittest -v
-- The answers run in order, so each one sees the changes made by the ones before it.

-- Q1: Create the members table described in the README.
CREATE TABLE members (
  id    INTEGER PRIMARY KEY,
  name  TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE
);


-- Q2: Create the classes table described in the README.
CREATE TABLE classes (
  id        INTEGER PRIMARY KEY,
  name      TEXT NOT NULL,
  starts_at TEXT NOT NULL,
  capacity  INTEGER NOT NULL CHECK (capacity > 0)
);


-- Q3: Create the bookings table described in the README.
CREATE TABLE bookings (
  member_id INTEGER NOT NULL REFERENCES members(id),
  class_id  INTEGER NOT NULL REFERENCES classes(id),
  booked_on TEXT NOT NULL,
  PRIMARY KEY (member_id, class_id)
);


-- Q4: With the example data from the README added, list each class's name and how many people have
--     booked it, A to Z.
INSERT INTO members (id, name, email) VALUES (1, 'Nadia Hussain', 'nadia@example.com'), (2, 'Ben Carter', 'ben@example.com');
INSERT INTO classes (id, name, starts_at, capacity) VALUES (1, 'Spin', '2025-09-01 07:00', 12), (2, 'Yoga', '2025-09-01 18:30', 20);
INSERT INTO bookings (member_id, class_id, booked_on) VALUES (1, 1, '2025-08-28'), (2, 1, '2025-08-29'), (1, 2, '2025-08-30');

SELECT c.name, COUNT(b.member_id)
FROM classes AS c
LEFT JOIN bookings AS b ON b.class_id = c.id
GROUP BY c.id
ORDER BY c.name;
