-- Select month 
-- Use case statement to determine res column 
-- from quarterof table

SELECT
  month,
  CASE
    WHEN month BETWEEN 1 AND 3 THEN 1
    WHEN month BETWEEN 4 AND 6 THEN 2
    WHEN month BETWEEN 7 AND 9 THEN 3
    WHEN month BETWEEN 10 AND 12 THEN 4
  END AS res
FROM quarterof;