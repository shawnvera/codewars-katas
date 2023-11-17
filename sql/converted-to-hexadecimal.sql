/*  Use the to_hex PostGreSQL function  */
SELECT to_hex(legs) AS legs, to_hex(arms) AS arms
FROM monsters;