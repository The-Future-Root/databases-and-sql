-- Lesson 1: your first queries
--
-- Write each answer under its question. Run them all with:
--     python3 ../run.py exercise.sql
-- and check them with:
--     python3 -m unittest -v

-- Q1: Show every column of every customer.
SELECT * FROM customers;


-- Q2: Show the title and author of every book.
SELECT title, author FROM books;


-- Q3: Show the id, customer_id and status of every order.
SELECT id, customer_id, status FROM orders;
