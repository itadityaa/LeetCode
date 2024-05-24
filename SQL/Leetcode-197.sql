SELECT w1.Id
FROM Weather w1
JOIN Weather w2 ON w1.RecordDate = w2.RecordDate + INTERVAL '1 day'
WHERE w1.Temperature > w2.Temperature;

-- Concepts:
-- 1. SQL JOIN
-- 2. SQL WHERE
-- 3. SQL INTERVAL
