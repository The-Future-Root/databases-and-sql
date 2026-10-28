-- Lesson 4: creating tables and adding rows
--
-- Write each answer under its question. Run them all with:
--     python3 ../run.py exercise.sql
-- and check them with:
--     python3 -m unittest -v
-- The answers run in order, so each one sees the changes made by the ones before it.

-- Q1: Create the reviews table described in the README.
CREATE TABLE reviews (
  id          INTEGER PRIMARY KEY,
  book_id     INTEGER NOT NULL REFERENCES books(id),
  customer_id INTEGER NOT NULL REFERENCES customers(id),
  rating      INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
  comment     TEXT,
  reviewed_on TEXT NOT NULL
);


-- Q2: Add the three reviews listed in the README. Let the database choose each id.
INSERT INTO reviews (book_id, customer_id, rating, comment, reviewed_on) VALUES
  (5, 1, 5, 'Changed how I think about history.', '2025-04-20'),
  (19, 3, 4, 'A lovely, gentle read.', '2025-06-02'),
  (8, 6, 3, NULL, '2025-06-14');


-- Q3: Add the new book listed in the README. Let the database choose its id.
INSERT INTO books (title, author, genre, price, stock, published)
VALUES ('Tomorrow, and Tomorrow, and Tomorrow', 'Gabrielle Zevin', 'Fiction', 10.99, 6, 2022);


-- Q4: Add the new customer listed in the README.
INSERT INTO customers (name, email, city, joined_on)
VALUES ('Ella Brooks', 'ella.brooks@example.com', 'York', '2025-07-12');
