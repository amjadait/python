#!/usr/bin/env python
# coding: utf-8

# # 1)

# In[5]:


def file(filez):
    txt = open(filez)
    print(txt.read())
file('python.txt')


# # 2)

# In[7]:


f = open("python.txt",'r',encoding = 'utf-8')
f.read(4)   


# # 3)

# In[8]:


f = open("python.txt",'r',encoding = 'utf-8')
f.read() 


# # 4)

# In[ ]:


def words(filepath):
    with open(filepath) as f:
        read = f.read

