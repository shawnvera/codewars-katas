-- BEGIN
-- batting avg = hits / at_bats
-- display batting avg as a 3 digit decimal
-- batting avg col must be a string
-- use CAST to convert and ROUND
-- only show results where the at bats are equal to or greater than 100
-- order by the batting average in DESC order
-- END

SELECT
  player_name,
  games,
  CAST(ROUND(CAST(hits AS DECIMAL) / CAST(at_bats AS DECIMAL), 3) AS TEXT) AS batting_average
FROM
  yankees
WHERE
  at_bats >= 100
ORDER BY
  batting_average DESC;