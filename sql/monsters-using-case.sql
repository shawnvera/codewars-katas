SELECT
  th.id,
  heads,
  legs,
  arms,
  tails,
CASE
  WHEN heads > arms OR tails > legs THEN 'BEAST'
  ELSE 'WEIRDO'
END AS species
FROM top_half th
LEFT JOIN bottom_half bh
  ON th.id = bh.id
ORDER BY species;