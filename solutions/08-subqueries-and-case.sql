-- Lesson 8: subqueries, CASE and WITH
--
-- Write each answer under its question. Run them all with:
--     python3 ../run.py exercise.sql
-- and check them with:
--     python3 -m unittest -v

-- Q1: The title and price of books that cost more than the average book, most expensive first, then
--     title A to Z.
SELECT title, price
FROM books
WHERE price > (SELECT AVG(price) FROM books)
ORDER BY price DESC, title;


-- Q2: The name of every customer who has placed at least one order, A to Z. Use IN with a subquery.
SELECT name
FROM customers
WHERE id IN (SELECT customer_id FROM orders)
ORDER BY name;


-- Q3: Each book's title, price and price band (call it band): 'budget' under 8, 'premium' 12 or
--     more, and 'standard' for everything else. Cheapest first, then title A to Z.
SELECT title, price,
       CASE
         WHEN price < 8 THEN 'budget'
         WHEN price >= 12 THEN 'premium'
         ELSE 'standard'
       END AS band
FROM books
ORDER BY price, title;


-- Q4: How many books are 'out of stock' (0), 'low' (1 to 4) and 'fine' (5 or more)? The label (call
--     it level) and the count, label A to Z.
SELECT CASE
         WHEN stock = 0 THEN 'out of stock'
         WHEN stock < 5 THEN 'low'
         ELSE 'fine'
       END AS level,
       COUNT(*)
FROM books
GROUP BY level
ORDER BY level;


-- Q5: The average value of a delivered order, rounded to 2 places. Work out each order's total in a
--     WITH query first.
WITH order_totals AS (
  SELECT i.order_id, SUM(i.quantity * i.unit_price) AS total
  FROM order_items AS i
  JOIN orders AS o ON o.id = i.order_id
  WHERE o.status = 'delivered'
  GROUP BY i.order_id
)
SELECT ROUND(AVG(total), 2)
FROM order_totals;


-- Q6: The name of the customer who placed the most recent order, and its date.
SELECT c.name, o.ordered_on
FROM orders AS o
JOIN customers AS c ON c.id = o.customer_id
WHERE o.ordered_on = (SELECT MAX(ordered_on) FROM orders);
