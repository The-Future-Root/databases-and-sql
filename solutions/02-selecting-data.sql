-- Lesson 2: choosing and sorting columns
--
-- Write each answer under its question. Run them all with:
--     python3 ../run.py exercise.sql
-- and check them with:
--     python3 -m unittest -v

-- Q1: The title and price of every book, most expensive first. Break ties by title, A to Z.
SELECT title, price
FROM books
ORDER BY price DESC, title;


-- Q2: The title and price of the 5 cheapest books, cheapest first.
SELECT title, price
FROM books
ORDER BY price
LIMIT 5;


-- Q3: Every genre, listed once each, A to Z.
SELECT DISTINCT genre
FROM books
ORDER BY genre;


-- Q4: Each book's title and the value of its stock (price times stock, rounded to 2 places) as
--     stock_value. Biggest value first, then title A to Z.
SELECT title, ROUND(price * stock, 2) AS stock_value
FROM books
ORDER BY stock_value DESC, title;


-- Q5: The name and joined_on date of the 3 customers who joined most recently, newest first.
SELECT name, joined_on
FROM customers
ORDER BY joined_on DESC
LIMIT 3;


-- Q6: Every city customers live in, listed once each, A to Z.
SELECT DISTINCT city
FROM customers
ORDER BY city;
