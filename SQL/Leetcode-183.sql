-- My solution
SELECT name Customers
FROM Customers 
WHERE id NOT IN
(SELECT c.id 
FROM Customers c
INNER JOIN Orders o ON c.id = o.customerId
);

-- Concepts:
-- 1. SQL Subquery
-- 2. SQL JOIN- Inner Join

--  Solution(s) by ChatGPT

--  ALTERNATIVE SOLUTION
-- Performance: In some databases, LEFT JOIN with NULL check can be optimized better than a subquery with NOT IN, especially when dealing with large datasets.
SELECT name Customers
FROM Customers
LEFT JOIN Orders
ON Customers.id = Orders.customerId
WHERE Orders.customerId IS NULL;

-- Concepts:
-- 1. SQL JOIN- Left Join
-- 2. SQL WHERE Clause
-- 3. SQL IS NULL

--  ALTERNATIVE SOLUTION
SELECT name Customers
FROM Customers
WHERE id NOT IN
(SELECT customerId
FROM Orders
);

-- Concepts:
-- 1. SQL Subquery
-- 2. SQL WHERE Clause
-- 3. SQL NOT IN