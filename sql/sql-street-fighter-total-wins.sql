-- Select name, sum of won, sum of lost from figthers. 
-- Need to use f. in front due to alias being used to simplify code
-- Perform an inner join on the fighters table with the winning_moves table where move_id is equal to id
-- Filter results based upon winning_moves id NOT IN 
-- Filter results can also be based upon specified moves not like the elements in the array - example commented out in the code below.
-- group by name
-- order by won in descending order
-- limit the return to top 6


SELECT name, SUM(f.won) AS won, SUM(f.lost) AS lost
from fighters f
JOIN winning_moves wm 
  ON f.move_id = wm.id
WHERE wm.id NOT IN (1, 2, 3)
-- WHERE wm.move NOT LIKE ALL(ARRAY['Hadoken','Shouoken', 'Kikoken']) 
GROUP BY name
ORDER BY won DESC
LIMIT 6;