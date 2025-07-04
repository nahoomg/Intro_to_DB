
-- task_4.sql

-- Use the alx_book_store database
USE ALX_BOOK_STORE;

-- Prints the full description of the 'books' table
-- by querying the INFORMATION_SCHEMA.COLUMNS table.
-- This is used as an alternative to DESCRIBE or EXPLAIN.
SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books'
ORDER BY
    ORDINAL_POSITION;