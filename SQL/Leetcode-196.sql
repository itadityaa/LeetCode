DELETE FROM Person
WHERE id NOT IN (
    SELECT MIN(id)
    FROM Person
    GROUP BY email
);

-- Concepts:
-- 1. SQL DELETE
-- 2. SQL Subquery
-- 3. SQL GROUP BY
-- 4. SQL MIN