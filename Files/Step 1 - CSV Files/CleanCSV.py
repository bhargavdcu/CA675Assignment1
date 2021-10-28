#!/usr/bin/env python
# coding: utf-8

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


# In[ ]:




