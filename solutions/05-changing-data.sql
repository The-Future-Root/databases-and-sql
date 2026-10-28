-- Lesson 5: changing and deleting rows
--
-- Write each answer under its question. Run them all with:
--     python3 ../run.py exercise.sql
-- and check them with:
--     python3 -m unittest -v
-- The answers run in order, so each one sees the changes made by the ones before it.

-- Q1: Dune's price has gone up to 11.49. Change it.
UPDATE books
SET price = 11.49
WHERE title = 'Dune';


-- Q2: Order 23 has just been posted. Set its status to 'shipped'.
UPDATE orders
SET status = 'shipped'
WHERE id = 23;


-- Q3: A delivery has arrived: add 10 to the stock of every book that has none.
UPDATE books
SET stock = stock + 10
WHERE stock = 0;


-- Q4: Summer sale: take 10% off every Classics book, rounding the new price to 2 places.
UPDATE books
SET price = ROUND(price * 0.9, 2)
WHERE genre = 'Classics';


-- Q5: Remove the cancelled orders completely: first their order_items, then the orders themselves.
DELETE FROM order_items
WHERE order_id IN (SELECT id FROM orders WHERE status = 'cancelled');

DELETE FROM orders
WHERE status = 'cancelled';


-- Q6: Add a phone column (TEXT) to customers, then set Priya Shah's phone to '0113 496 0000'.
ALTER TABLE customers ADD COLUMN phone TEXT;

UPDATE customers
SET phone = '0113 496 0000'
WHERE email = 'priya.shah@example.com';
