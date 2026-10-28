# Tests for this lesson. Run them from this folder with:  python3 -m unittest -v
# Each test runs your answer from exercise.sql on a fresh copy of the database.
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from sqltest import SqlLesson  # noqa: E402


class TestLesson(SqlLesson):
    cumulative = True

    def test_q1(self):
        self.check_after(1, "SELECT name FROM pragma_index_info('idx_orders_customer');", [('customer_id',)])

    def test_q2(self):
        self.check_after(2, "EXPLAIN QUERY PLAN SELECT title FROM books WHERE author = 'Andy Weir';", [(3, 0, 0, 'SEARCH books USING INDEX idx_books_author (author=?)')])

    def test_q3(self):
        self.check_after(3, "SELECT (SELECT COUNT(*) FROM orders WHERE id = 27 AND customer_id = 4 AND ordered_on = '2025-07-12' AND status = 'pending'), (SELECT quantity || ' at ' || unit_price FROM order_items WHERE order_id = 27 AND book_id = 1), (SELECT stock FROM books WHERE id = 1);", [(1, '2 at 9.99', 12)])
        self.check_uses(3, '\\bBEGIN\\b', 'start with BEGIN')
        self.check_uses(3, '\\bCOMMIT\\b', 'finish with COMMIT')

    def test_q4(self):
        self.check_after(4, 'SELECT COUNT(*) FROM order_items;', [(46,)])
        self.check_uses(4, '\\bDELETE\\s+FROM\\s+order_items\\b', 'delete from order_items inside the transaction')
        self.check_uses(4, '\\bROLLBACK\\b', 'use ROLLBACK to undo it')


if __name__ == "__main__":
    unittest.main()
