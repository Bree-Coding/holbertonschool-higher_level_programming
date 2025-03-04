-- Lists all records of the table second_table, sorted by score in descending order, but without the link to the documentation

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
