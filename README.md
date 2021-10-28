# CA675Assignment1
Assignment 1

# Files Structure
 1) CSV Files </br>
    Contains all CSV files obtained from query as well as cleaned files.Also contains python code used for cleaning
  
2) Hadoop and Pig Code </br>
    Contains Hadoop and Pig Code for replace function and loading-unloading from HDFS

3) Hive Code </br> 
    Contains HQL code for table creation and loading of data into the table

4) Query Results </br>
    Contains code for queries and output from the respective queries

5) TF-IDF </br> 
   Contains Mapper-Reducer files and rest of the steps for obtaining TF-IDF </br> 
   TF-IDF Reference: https://github.com/SatishUC15/TFIDF-HadoopMapReduce </br>
   Description - https://monkeylearn.com/blog/what-is-tf-idf/ </br>
   Query - https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-row_number-function/</br>

6) Screenshots - Contains screenshots

# Important Snippets

```
# SQL Queries

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

```
# Python Code

# In[8]:
import pandas as pd;
# In[9]:
stack_posts = pd.read_csv("/home/sunny/675_Submission/FQ.csv")
# In[10]:
stack_posts.head()
# In[13]:

#To Clean Body Column
stack_posts['Body'] = stack_posts['Body'].str.replace(r'\n','',regex=True)
stack_posts['Body'] = stack_posts['Body'].str.replace('[^A-Za-z0-9 ]+',' ',regex=True)
#To Clean Title Column
stack_posts['Title'] = stack_posts['Title'].str.replace(r'\n','',regex=True)
stack_posts['Title'] = stack_posts['Title'].str.replace('[^A-Za-z0-9 ]+',' ',regex=True)

# In[14]:
stack_posts.head()
# In[16]:
stack_posts.to_csv('FQ_Stack.csv', index=False)
```

```
# Hive Create Table

CREATE TABLE stackposts_cleaned
(
post_id int,
post_type int, 
acc_ans_id int,
parent_id int,
cre_date timestamp,
del_date timestamp,
score int,
view_count int,
body string,
owner_id int,
owner_name string,
ls_edi_user_id int,
ls_edi_disname string,
last_edit_date timestamp,
last_act_date timestamp,
title string,
tags string,
ans_count int,
comment_count int,
fav_count int,
clo_date timestamp,
comm_own_date timestamp,
content_license string,
dis_name string
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
```

