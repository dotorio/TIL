CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date DATE,
  total_amount REAL
);

INSERT INTO orders (order_date, total_amount) VALUES 
('2024-04-02', 25.99),
('2024-04-01', 35.50),
('2024-03-30', 15.75);

SELECT
  *
FROM
  orders;

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name Text,
  email Text,
  phone Text
);

INSERT INTO customers (name, email, phone)
VALUES
('허균', 'h.gd@aaa.com', '010-1234-1234'),
('김영희', 'k.yh@aaa.com', '010-1234-5678'),
('이철수', 'l.cs@aaa.com', '010-1234-2345');

SELECT
  *
FROM
  customers;

DELETE FROM
  orders
WHERE
  order_id = 3;

UPDATE
  customers
SET
  name = '홍길동'
WHERE
  customer_id = 1;

