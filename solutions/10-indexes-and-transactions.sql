-- Lesson 10: indexes and transactions
--
-- Write each answer under its question. Run them all with:
--     python3 ../run.py exercise.sql
-- and check them with:
--     python3 -m unittest -v
-- The answers run in order, so each one sees the changes made by the ones before it.

-- Q1: Create an index called idx_orders_customer on the customer_id column of orders.
CREATE INDEX idx_orders_customer ON orders (customer_id);


-- Q2: Create an index called idx_books_author so that searching books by author can use it.
CREATE INDEX idx_books_author ON books (author);


-- Q3: Record a new order in one transaction: order 27 for customer 4 on '2025-07-12' with status
--     'pending', containing 2 copies of The Hobbit (book 1) at 9.99, and take those 2 copies off
--     The Hobbit's stock.
BEGIN;

INSERT INTO orders (id, customer_id, ordered_on, status)
VALUES (27, 4, '2025-07-12', 'pending');

INSERT INTO order_items (order_id, book_id, quantity, unit_price)
VALUES (27, 1, 2, 9.99);

UPDATE books
SET stock = stock - 2
WHERE id = 1;

COMMIT;


-- Q4: Start a transaction, delete every row in order_items, then change your mind and undo it, so
--     nothing is lost.
BEGIN;

DELETE FROM order_items;

ROLLBACK;
