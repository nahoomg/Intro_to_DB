-- task_5.sql

-- Use the alx_book_store database
USE ALX_BOOK_STORE;

-- Inserts a single row into the Customers table.
INSERT INTO Customer (
    customer_id,
    customer_name,
    email,
    address
) VALUES (
    1,
    'Cole Baidoo',
    'cbaidoo@sandtech.com',
    '123 Happiness Ave.'
);