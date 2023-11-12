-- INITCAP returns the argument with the first letter capitalized
-- Concatenate the fist and last names into one column labeld 'shortlist'
-- Separate the first and last name with a space

SELECT CONCAT(INITCAP(firstname), ' ', INITCAP(lastname)) AS shortlist
FROM Elves
-- % need to be on both sides of the search criteria
WHERE firstname LIKE '%tegil%'
OR lastname LIKE '%astar%';