-- bookshop.sql: the example database for this course.
-- Build it with:  python3 ../run.py --reset   (or: sqlite3 bookshop.db < bookshop.sql)

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
  id        INTEGER PRIMARY KEY,
  name      TEXT NOT NULL,
  email     TEXT NOT NULL UNIQUE,
  city      TEXT,
  joined_on TEXT NOT NULL
);

CREATE TABLE books (
  id        INTEGER PRIMARY KEY,
  title     TEXT NOT NULL,
  author    TEXT NOT NULL,
  genre     TEXT NOT NULL,
  price     REAL NOT NULL CHECK (price > 0),
  stock     INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
  published INTEGER
);

CREATE TABLE orders (
  id          INTEGER PRIMARY KEY,
  customer_id INTEGER NOT NULL REFERENCES customers(id),
  ordered_on  TEXT NOT NULL,
  status      TEXT NOT NULL CHECK (status IN ('pending', 'shipped', 'delivered', 'cancelled'))
);

CREATE TABLE order_items (
  order_id   INTEGER NOT NULL REFERENCES orders(id),
  book_id    INTEGER NOT NULL REFERENCES books(id),
  quantity   INTEGER NOT NULL CHECK (quantity > 0),
  unit_price REAL NOT NULL,
  PRIMARY KEY (order_id, book_id)
);

INSERT INTO customers (id, name, email, city, joined_on) VALUES
  (1, 'Priya Shah', 'priya.shah@example.com', 'Leeds', '2024-02-11'),
  (2, 'Tom Becker', 'tom.becker@example.com', 'Manchester', '2024-03-02'),
  (3, 'Aisha Bello', 'aisha.bello@example.com', 'London', '2024-03-19'),
  (4, 'Daniel Okafor', 'daniel.okafor@example.com', 'Leeds', '2024-05-07'),
  (5, 'Mei Lin', 'mei.lin@example.com', 'Bristol', '2024-06-23'),
  (6, 'Lucas Moreau', 'lucas.moreau@example.com', 'London', '2024-08-14'),
  (7, 'Hannah Fischer', 'hannah.fischer@example.com', NULL, '2024-09-01'),
  (8, 'Omar Haddad', 'omar.haddad@example.com', 'Manchester', '2024-11-30'),
  (9, 'Sofia Rossi', 'sofia.rossi@example.com', 'Bristol', '2025-01-08'),
  (10, 'Jack Wilson', 'jack.wilson@example.com', 'London', '2025-02-17'),
  (11, 'Grace Kim', 'grace.kim@example.com', 'Leeds', '2025-03-05'),
  (12, 'Ravi Patel', 'ravi.patel@example.com', 'Glasgow', '2025-03-28');

INSERT INTO books (id, title, author, genre, price, stock, published) VALUES
  (1, 'The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 9.99, 14, 1937),
  (2, 'Dune', 'Frank Herbert', 'Science Fiction', 10.99, 8, 1965),
  (3, 'Pride and Prejudice', 'Jane Austen', 'Classics', 6.99, 20, 1813),
  (4, 'The Martian', 'Andy Weir', 'Science Fiction', 9.49, 5, 2011),
  (5, 'Sapiens', 'Yuval Noah Harari', 'Non-fiction', 12.99, 11, 2011),
  (6, 'Atomic Habits', 'James Clear', 'Non-fiction', 14.99, 0, 2018),
  (7, 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Crime', 8.99, 6, 2005),
  (8, 'Gone Girl', 'Gillian Flynn', 'Crime', 8.49, 3, 2012),
  (9, 'Nineteen Eighty-Four', 'George Orwell', 'Classics', 7.99, 17, 1949),
  (10, 'Project Hail Mary', 'Andy Weir', 'Science Fiction', 11.99, 9, 2021),
  (11, 'The Fellowship of the Ring', 'J.R.R. Tolkien', 'Fantasy', 10.99, 7, 1954),
  (12, 'Educated', 'Tara Westover', 'Non-fiction', 10.49, 4, 2018),
  (13, 'The Thursday Murder Club', 'Richard Osman', 'Crime', 9.99, 12, 2020),
  (14, 'Frankenstein', 'Mary Shelley', 'Classics', 5.99, 10, 1818),
  (15, 'A Brief History of Time', 'Stephen Hawking', 'Non-fiction', 11.49, 2, 1988),
  (16, 'The Name of the Wind', 'Patrick Rothfuss', 'Fantasy', 10.49, 0, 2007),
  (17, 'Klara and the Sun', 'Kazuo Ishiguro', 'Fiction', 12.49, 6, 2021),
  (18, 'Normal People', 'Sally Rooney', 'Fiction', 9.99, 8, 2018),
  (19, 'The Midnight Library', 'Matt Haig', 'Fiction', 9.49, 15, 2020),
  (20, 'Thinking, Fast and Slow', 'Daniel Kahneman', 'Non-fiction', 13.49, 5, 2011);

INSERT INTO orders (id, customer_id, ordered_on, status) VALUES
  (1, 1, '2025-04-06', 'delivered'),
  (2, 6, '2025-04-10', 'delivered'),
  (3, 1, '2025-04-11', 'delivered'),
  (4, 1, '2025-04-15', 'delivered'),
  (5, 8, '2025-04-16', 'delivered'),
  (6, 3, '2025-04-22', 'delivered'),
  (7, 1, '2025-04-27', 'cancelled'),
  (8, 6, '2025-04-29', 'delivered'),
  (9, 1, '2025-05-02', 'delivered'),
  (10, 4, '2025-05-07', 'delivered'),
  (11, 9, '2025-05-13', 'delivered'),
  (12, 3, '2025-05-21', 'delivered'),
  (13, 3, '2025-05-26', 'delivered'),
  (14, 2, '2025-05-31', 'delivered'),
  (15, 3, '2025-06-01', 'delivered'),
  (16, 3, '2025-06-06', 'delivered'),
  (17, 2, '2025-06-08', 'delivered'),
  (18, 1, '2025-06-09', 'delivered'),
  (19, 3, '2025-06-15', 'cancelled'),
  (20, 8, '2025-06-20', 'shipped'),
  (21, 6, '2025-06-22', 'shipped'),
  (22, 5, '2025-06-25', 'shipped'),
  (23, 6, '2025-06-29', 'pending'),
  (24, 3, '2025-07-01', 'delivered'),
  (25, 5, '2025-07-07', 'delivered'),
  (26, 9, '2025-07-10', 'delivered');

INSERT INTO order_items (order_id, book_id, quantity, unit_price) VALUES
  (1, 6, 1, 14.99),
  (1, 18, 1, 9.99),
  (2, 13, 2, 9.99),
  (3, 13, 1, 9.99),
  (4, 19, 3, 9.49),
  (5, 7, 1, 7.19),
  (6, 12, 3, 10.49),
  (6, 16, 1, 10.49),
  (7, 7, 1, 8.99),
  (8, 5, 3, 12.99),
  (9, 9, 3, 7.99),
  (9, 16, 1, 10.49),
  (9, 20, 1, 13.49),
  (10, 3, 3, 6.99),
  (10, 13, 2, 9.99),
  (11, 11, 3, 10.99),
  (12, 19, 3, 7.59),
  (13, 10, 1, 11.99),
  (13, 11, 1, 10.99),
  (14, 9, 3, 7.99),
  (14, 19, 1, 9.49),
  (15, 5, 3, 12.99),
  (15, 19, 2, 9.49),
  (15, 20, 1, 13.49),
  (16, 1, 1, 9.99),
  (16, 15, 1, 11.49),
  (16, 18, 1, 9.99),
  (17, 5, 1, 12.99),
  (17, 20, 3, 13.49),
  (18, 5, 1, 12.99),
  (18, 7, 1, 8.99),
  (19, 5, 2, 12.99),
  (19, 12, 1, 10.49),
  (20, 18, 1, 9.99),
  (21, 1, 1, 9.99),
  (21, 8, 3, 8.49),
  (21, 19, 1, 9.49),
  (22, 3, 1, 6.99),
  (22, 5, 3, 12.99),
  (23, 4, 1, 9.49),
  (23, 11, 3, 10.99),
  (24, 5, 2, 12.99),
  (24, 8, 1, 8.49),
  (25, 6, 1, 14.99),
  (26, 20, 1, 13.49);
