Insert new rows into a table

```
INSERT INTO table_name VALUES (value_1, value_2,....)

INSERT INTO table_name (column1, column2,...) VALUES (value_1, value_2,....)
```

Update one or several rows in a table.

```
UPDATE table_name 
SET column_name_1 = new_value_1, column_name_2 = new_value_2
WHERE column_name = some_value
```

Delete rows in a table.

```
DELETE FROM table_name
WHERE column_name = some_value		
```

Deletes all data inside the table.

```
TRUNCATE TABLE table_name
```	

Create **View** (a virtual table) based on the result-set of a SELECT statement.

```
CREATE VIEW view_name AS
SELECT column_name(s)
FROM table_name
WHERE condition
```