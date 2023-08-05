#!/usr/bin/env python
# coding: utf-8

# # 1)

# In[2]:


import pandas as pd
import numpy as np



exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']



df = pd.DataFrame(exam_data, index =labels)

print(df.head(3))



# # 2)

# In[3]:


df = df.dropna(how='any')


# In[4]:


df


# # 3)

# In[5]:


rowk = {'name': 'Suresh', 'score': 15.5, 'attempts': 1, 'qualify': 'yes'}
df1 = pd.DataFrame(rowk, index = ['k'])


# In[6]:


df1


# In[7]:


df = pd.concat([df, df1])


# # 4)

# In[8]:


df = df.drop('attempts', axis=1)


# In[9]:


df


# # 5)

# In[10]:


df['Success'] = df['score'].apply(lambda x: 1 if x > 10 else 0)


# In[11]:


df


# # 6)

# In[14]:


df.to_csv('my_data.csv')

