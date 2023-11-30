SELECT DISTINCT capital
FROM countries
WHERE (continent LIKE 'Africa' 
  OR continent LIKE 'Afrika') 
  AND country LIKE 'E%'
ORDER BY capital
LIMIT 3;