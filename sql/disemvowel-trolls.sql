-- Use SQL string function TRANSLATE to replace any element in the 1st argument str that matches the 2nd argument of vowels with the 3rd argument of ''
SELECT str, TRANSLATE(str, 'AEIOUaeiou', '') AS res
FROM disemvowel;