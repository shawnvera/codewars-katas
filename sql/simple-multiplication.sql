-- use CASE to test whether the number is even with modulo 
-- if even multipy number by 8
-- else multiply by 9

SELECT
  number,
  CASE
    WHEN number % 2 = 0 THEN number * 8
    ELSE number * 9
  END AS res
FROM multiplication;