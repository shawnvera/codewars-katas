SELECT
  p.pokemon_name,
  (p.str * m.multiplier) AS modifiedstrength,
  m.element
FROM pokemon p
LEFT JOIN multipliers m
  ON m.id = p.element_id
WHERE (p.str * m.multiplier) > 40
ORDER BY (p.str * m.multiplier) DESC;