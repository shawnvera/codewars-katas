-- use RANK() function over the COUNT of sales id in descending order
SELECT
  p.id,
  p.name,
  COUNT(s.id) AS sale_count,
  RANK() OVER (ORDER BY COUNT(s.id) DESC) AS sale_rank
FROM people p
LEFT JOIN sales s
  ON s.people_id = p.id
GROUP BY p.id
ORDER BY sale_count DESC;