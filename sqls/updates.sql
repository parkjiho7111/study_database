-- UPDATE Syntax
-- UPDATE table_name
-- SET column1 = value1, column2 = value2, ...
-- WHERE condition;


UPDATE persons
SET lastname = 'smith', firstname = 'black'
WHERE personid = 2;