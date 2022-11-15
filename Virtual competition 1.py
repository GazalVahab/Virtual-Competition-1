#!/usr/bin/env python
# coding: utf-8

# Consider the following Python dictionary `data` and Python list `labels`:
# 
# ``` python
# data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
#         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
#         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
# 
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# ```
# 
# **1.** Create a DataFrame `df` from this dictionary `data` which has the index `labels`.

# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[7]:


import pandas as pd
import numpy as np
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data , index=labels)
print(df)


# **2.** Display a summary of the basic information about this DataFrame and its data (*hint: there is a single method that can be called on the DataFrame*).

# In[8]:


df.describe()


# In[9]:


df.info()


# **3.** Return the first 3 rows of the DataFrame `df`.

# In[16]:


df = pd.DataFrame(data)
df1 = df.head(3)
df1


# **4.** Display the 'animal' and 'age' columns from the DataFrame `df`

# In[17]:


df = pd.DataFrame(data)
df[['animal', 'age']]


# **5.** Display the data in rows `[3, 4, 8]` *and* in columns `['animal', 'age']'

# In[38]:


df.iloc[3,0:2]


# In[39]:


df.iloc[4,0:2]


# In[40]:


df.iloc[8,0:2]


# **6.** Select only the rows where the number of visits is greater than 3.

# In[108]:


convert={'age': float,'visits': int}

df = df.astype(convert)
print(df.dtypes)
df = pd.DataFrame(data)
df2=df.loc[df['visits'] >=3]
df2


# **7.** Select the rows where the age is missing, i.e. it is `NaN`.

# In[104]:


df[df['age'].isnull()]
#df.loc[df['age'] == '']


# **8.** Select the rows where the animal is a cat *and* the age is less than 3.

# In[72]:


df.loc[(df['animal'] == 'cat') | (df['age'] <= 3)]


# **9.** Select the rows where the age is between 2 and 4 (inclusive)

# In[105]:


df.loc[(df['age'] <= 2) | (df['age'] <= 4)]


# **10.** Change the age in row 'f' to 1.5.

# In[133]:


df['age'].replace([2.0], 1.5)


# **11.** Calculate the sum of all visits in `df` (i.e. the total number of visits).

# In[115]:


df.sum(axis=0)


# **12.** Calculate the mean age for each different animal in `df`.

# In[117]:


df.mean(axis=0)


# **13.** Append a new row 'k' to `df` with your choice of values for each column. Then delete that row to return the original DataFrame.

# In[162]:


data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data , index=labels)
df2 = {'animal': 'cat', 'visits': 2, 'priority': 'no'}
df1=df.append(df2,ignore_index=True)
df1


# **14.** Count the number of each type of animal in `df`.

# In[121]:


df.groupby(['animal']).size()


# **15.** Sort `df` first by the values in the 'age' in *decending* order, then by the value in the 'visits' column in *ascending* order (so row `i` should be first, and row `d` should be last).

# In[125]:


df.sort_values(by='age', ascending=False)
df.sort_values(by='visits')


# In[123]:


df.sort_values(by='visits')


# **16.** The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes' should be `True` and 'no' should be `False`.

# In[129]:


df['priority'].map({'yes':True ,'no':False})


# **17.** In the 'animal' column, change the 'snake' entries to 'python'.

# In[130]:


df['animal'].replace(['snake'], 'python')


# **18.** Load the ny-flights dataset to Python

# In[152]:


data1=pd.read_csv("C:/Users/Wahab/Documents/DSA/ny-flights.csv")
data1


# **19.** Which airline ID is present maximum times in the dataset

# In[153]:


data1['airline_id'].value_counts()


# **20.** Draw a plot between dep_delay and arr_delay

# In[154]:


plt.bar(data1['dep_delay'],data['arr_delay'])
plt.show()


# In[ ]:




