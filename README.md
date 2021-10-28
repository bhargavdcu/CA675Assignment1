# CA675Assignment1
Assignment 1

# Files Structure
1) CSV Files - Contains all CSV files obtained from query as well as cleaned files.Also contains python code used for cleaning
  
2) Hadoop and Pig Code - Contains Hadoop and Pig Code for replace function and loading-unloading from HDFS

3) Hive Code - Contains HQL code for table creation and loading of data into the table

4) Query Results - Contains code for queries and output from the respective queries

5) TFIDF - Contains Mapper-Reducer files and rest of the steps for obtaining TF-IDF. 


   TF-IDF Reference: https://github.com/SatishUC15/TFIDF-HadoopMapReduce

6) Screenshots - Contains screenshots

# Important Snippets

```
SQL Queries

Query 1
select top 50000 pos.*,usr.DisplayName from posts AS pos join users AS usr on pos.OwnerUserId=usr.Id ORDER BY pos.ViewCount DESC
 
Query 2
select top 50000 pos.*,usr.DisplayName from posts AS pos join users AS usr on 
 pos.OwnerUserId=usr.Id 
 and pos.ViewCount<124974 ORDER BY pos.ViewCount DESC
 
Query 3
select top 50000 pos.*,usr.DisplayName from posts AS pos join users AS usr on 
pos.OwnerUserId=usr.Id 
 and pos.ViewCount<73139 ORDER BY pos.ViewCount DESC
 
Query 4
select top 50000 pos.*,usr.DisplayName from posts AS pos join users AS usr on 
pos.OwnerUserId=usr.Id 
 and pos.ViewCount<52110 ORDER BY pos.ViewCount DESC
```
