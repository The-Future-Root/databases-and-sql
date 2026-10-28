-- Lesson 6: counting, totals and GROUP BY
--
-- Write each answer under its question. Run them all with:
--     python3 ../run.py exercise.sql
-- and check them with:
--     python3 -m unittest -v

-- Q1: How many books are there? Call the column book_count.
SELECT COUNT(*) AS book_count
FROM books;


-- Q2: In one row: the total stock, the average price (rounded to 2 places), the lowest price and
--     the highest price of all books.
SELECT SUM(stock), ROUND(AVG(price), 2), MIN(price), MAX(price)
FROM books;


-- Q3: For each genre: the genre, how many books it has, and their average price rounded to 2
--     places. Genres A to Z.
SELECT genre, COUNT(*), ROUND(AVG(price), 2)
FROM books
GROUP BY genre
ORDER BY genre;


-- Q4: The 5 biggest orders: order_id and total (quantity times unit_price, added up, rounded to 2
--     places) as total. Biggest first.
SELECT order_id, ROUND(SUM(quantity * unit_price), 2) AS total
FROM order_items
GROUP BY order_id
ORDER BY total DESC
LIMIT 5;


-- Q5: Cities with more than one customer: the city and the number of customers, A to Z. Use HAVING.
SELECT city, COUNT(*)
FROM customers
GROUP BY city
HAVING COUNT(*) > 1
ORDER BY city;


-- Q6: The number of orders in each month: the month as 'YYYY-MM' (call it month) and the count
--     (call it orders). Earliest month first.
SELECT substr(ordered_on, 1, 7) AS month, COUNT(*) AS orders
FROM orders
GROUP BY month
ORDER BY month;
