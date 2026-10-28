-- Lesson 7: joining tables
--
-- Write each answer under its question. Run them all with:
--     python3 ../run.py exercise.sql
-- and check them with:
--     python3 -m unittest -v

-- Q1: Every order with the name of the customer who placed it: order id, customer name and
--     ordered_on, by order id.
SELECT orders.id, customers.name, orders.ordered_on
FROM orders
JOIN customers ON customers.id = orders.customer_id
ORDER BY orders.id;


-- Q2: What's in order 3? The title, quantity and unit_price of each line, title A to Z.
SELECT books.title, order_items.quantity, order_items.unit_price
FROM order_items
JOIN books ON books.id = order_items.book_id
WHERE order_items.order_id = 3
ORDER BY books.title;


-- Q3: Every customer and how many orders they've placed, including customers with none: name and
--     order count. Most orders first, then name A to Z.
SELECT c.name, COUNT(o.id) AS order_count
FROM customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.id
GROUP BY c.id
ORDER BY order_count DESC, c.name;


-- Q4: The title of every book that has never been ordered.
SELECT b.title
FROM books AS b
LEFT JOIN order_items AS i ON i.book_id = b.id
WHERE i.book_id IS NULL;


-- Q5: How much each customer has spent on delivered orders: name and total spent (rounded to 2
--     places). Biggest spender first.
SELECT c.name, ROUND(SUM(i.quantity * i.unit_price), 2) AS spent
FROM customers AS c
JOIN orders AS o ON o.customer_id = c.id
JOIN order_items AS i ON i.order_id = o.id
WHERE o.status = 'delivered'
GROUP BY c.id
ORDER BY spent DESC;


-- Q6: Copies sold in each genre, counting every order except cancelled ones: genre and copies. Most
--     copies first, then genre A to Z.
SELECT b.genre, SUM(i.quantity) AS copies
FROM order_items AS i
JOIN books AS b ON b.id = i.book_id
JOIN orders AS o ON o.id = i.order_id
WHERE o.status <> 'cancelled'
GROUP BY b.genre
ORDER BY copies DESC, b.genre;
