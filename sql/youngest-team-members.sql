-- Define CTE (common table expression) ranked employees.
-- Use row_number to rank employees
-- Use partition by on the team and order by respective birth dates in
-- descending order. Store in column rank.
-- If you want to account for employees with the same birthday RANK() should
-- be used in place of ROW_NUMBER().

WITH RankedEmployees AS (
  SELECT
    employee_id,
    full_name,
    team,
    birth_date,
    ROW_NUMBER() OVER (PARTITION BY team ORDER BY birth_date DESC) AS rank
  FROM
    employees
)

SELECT
  employee_id,
  full_name,
  team,
  birth_date
FROM
  RankedEmployees
WHERE
  rank = 1
ORDER BY
  team;