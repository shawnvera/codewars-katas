-- concatenate column md 5 with the max length inserting "1" on each column
SELECT
    CONCAT(md5, REPEAT('1', MAX_LENGTH - LENGTH(md5))) AS md5,
    CONCAT(REPEAT('0', MAX_LENGTH - LENGTH(sha1)), sha1) AS sha1,
    sha256
FROM
    encryption,
    (SELECT MAX(LENGTH(sha256)) AS MAX_LENGTH FROM encryption) AS max_lengths;
