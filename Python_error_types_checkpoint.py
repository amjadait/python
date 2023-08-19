#!/usr/bin/env python
# coding: utf-8

# # Rectify the code in each cell and **explain the error in comments**

# ### index error

# In[1]:


mylist=[14, "hello", 967]
mylist[2]


# In[4]:


import pandas
import numpy


# # syntax error

# In[6]:


print("python errors")


# # key error

# In[7]:


mydictionnary={True:"hello",False:"bye", '3':"python"}
mydictionnary[True]


# # indentation error

# In[8]:


i=14
while i<78:
    print(i)
    i+=1


# # StopIteration

# In[9]:


it=iter([1,2,3])
next(it)
next(it)
next(it)


# # TypeError
# 

# In[10]:


15+15


# # ValueError

# In[11]:


str('python')


# # NameError

# In[12]:


python = int()


# # ZeroDivisionError

# In[14]:


x=19/9


# In[ ]:




