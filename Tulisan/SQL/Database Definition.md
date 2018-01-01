##Database##
Creating a new database

```
CREATE DATABASE database_name
```
Delete a database

```
DROP DATABASE database_name
```

##Table##
###Create Table###

```
CREATE TABLE "table_name" ("column_1" "data_type_for_column_1", "column_2" "data_type_for_column_2", ... )
```

Sample: 

```
CREATE TABLE Person (LastName varchar, FirstName varchar, Address varchar, Age int)
```

common datatype: 

```
integer(size)
int(size)
smallint(size)
tinyint(size)
decimal(size,d)
numeric(size,d)
char(size)
varchar(size)
date(yyyymmdd)
```

Create a new table by copying selected data from another table. Data type will be derived from source.

```
SELECT column_name(s)
INTO new_table_name
FROM source_table_name
WHERE query
```

###Modify Table Structure###

Add columns in an existing table.

```
ALTER TABLE table_name ADD column_name datatype		
```

Delete columns in an existing table.

```
ALTER TABLE table_name DROP column_name datatype	

```

###Delete a table###

```
DROP TABLE table_name					
```


##Index##

Create a simple index.

```
CREATE INDEX index_name ON table_name (column_name_1, column_name_2, ...)		
```

Create a unique index.

```
CREATE UNIQUE INDEX index_name ON table_name (column_name_1, column_name_2, ...)	
```

Delete an index.

```
DROP INDEX table_name.index_name			```