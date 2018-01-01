##Data Selection##

Select value from specific column

```
SELECT column_name FROM table_name;
```

Column name can be aliased

```
SELECT column_name AS alias FROM table_name;
```

Select from multiple column

```
SELECT column_name AS alias, column2_name AS alias, ..., columnx_name AS alias FROM table_name
```

Select all columns

```
SELECT * FROM table_name;
```

Select only distinct (unique) value

```
SELECT DISTINCT column_name(s) FROM table_name
```

##Conditions##

Common Operators

```
SELECT * FROM table_name
WHERE column_name = value;
```

operators:

```
=	    Equal
<>	    Not equal
>	    Greater than
<	    Less than
>=	    Greater than or equal
<=	    Less than or equal
```

Select between an inclusive range

```
SELECT * FROM table_name
WHERE column_name BETWEEN value1 and value2;
```

Select using wildcards (%)

```
SELECT * FROM table_name
WHERE column_name LIKE '%value%';
```

Select from lists

```
SELECT * FROM table_name
WHERE column_name IN (value1, value2, ...)
```

Use AND or OR to have multiple condition

```
SELECT * FROM table_name
WHERE column_name = value [AND|OR] column2_name [OPERATOR] value;
```

##Sorting##

Use Order By

```
SELECT column_name(s) FROM table_name
ORDER BY column_name [ASC|DESC], column2_name [ASC|DESC], ...
```

##Grouping##

Use GROUP BY to group the rows. Useful to do aggregate functions.

```
SELECT column_name_to_group, SUM(column_name_to_total)
FROM table_name
GROUP BY column_name_to_group;

Sample, to get total experience of employee:
	SELECT name, SUM(experience)
	FROM table_name
	GROUP BY experience
```

Aggregate functions:

```
AVG(column)		Returns the average value of a column
COUNT(column)	Returns the number of rows (without a NULL value) of a column
MAX(column)		Returns the highest value of a column
MIN(column)		Returns the lowest value of a column
SUM(column)		Returns the total sum of a column
```

##Having##

HAVING is to further filter the result after grouping and aggregating the data

```sql
SELECT column_1, ..., SUM(group_column_name)
FROM table_name
GROUP BY group_column_name
HAVING SUM(group_column_name) CONDITION value
```