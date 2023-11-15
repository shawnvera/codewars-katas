-- Select position and roll columns from moves
-- Select 3rd column 'res' with formula roll multiplied by 2 then add the position
-- Return a table with a column 'res' that has the value of the formula 

SELECT position, roll, (roll * 2) + position AS res
FROM moves;