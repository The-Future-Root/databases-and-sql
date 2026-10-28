-- Lesson 3: filtering rows with WHERE
--
-- Write each answer under its question. Run them all with:
--     python3 ../run.py exercise.sql
-- and check them with:
--     python3 -m unittest -v

-- Q1: The title and price of every Crime book.
SELECT title, price
FROM books
WHERE genre = 'Crime';


-- Q2: The title and price of every book under 9.50, cheapest first, then title A to Z.
SELECT title, price
FROM books
WHERE price < 9.5
ORDER BY price, title;


-- Q3: The title and genre of Fantasy and Science Fiction books that are in stock. Use IN.
SELECT title, genre
FROM books
WHERE genre IN ('Fantasy', 'Science Fiction')
  AND stock > 0;


-- Q4: The title and published year of books published from 2010 to 2019, oldest first, then title A
--     to Z. Use BETWEEN.
SELECT title, published
FROM books
WHERE published BETWEEN 2010 AND 2019
ORDER BY published, title;


-- Q5: The title of every book with the word 'the' anywhere in its title, in any case.
SELECT title
FROM books
WHERE title LIKE '%the%';


-- Q6: The name and email of customers whose city isn't known.
SELECT name, email
FROM customers
WHERE city IS NULL;


-- Q7: The id and status of every order that is still on its way: not delivered and not cancelled.
SELECT id, status
FROM orders
WHERE status NOT IN ('delivered', 'cancelled');
