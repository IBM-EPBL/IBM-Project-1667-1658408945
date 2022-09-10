#!/usr/bin/env python
# coding: utf-8

# # BASIC PYTHON

# 1.Split the string

# In[1]:


s="Hi there Sam!"
print(s.split())


# 2.Use.format() to print the following string

# Output should be:The diameter of Earth is 12742 kilometers

# In[2]:


print("The diameter of {planet} is {diameter} kilometers.".format(planet='Earth',diameter='12742'))


# In the Nest dictionary grab the word "hello"

# In[3]:


dict = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(dict['k1'][3]['tricky'][3]['target'][3])


# NUMPY

# 4.1 Create an array of 10 Zeros?
# 4.2 Create an array of 10 fives?

# In[19]:


import numpy as np


# In[6]:


#4.1
array=np.zeros(10)
print("An array of 10 Zeros : ",array)


# In[10]:


#4.2
array=np.ones(10)*5
print("An array of 10 Fives : ",array)


# 5.Create an array of all the even intergers from 20 to 35?

# In[13]:


array=np.arange(20,36,2)
print("An array of all the even intergers from 20 to 35 :",array)


# 6.Create a 3x3 matrix with values ranging from 0 to 8?

# In[15]:


matrix=np.arange(0,9).reshape(3,3)
print(matrix)


# 7.Concatenate a and b
# a=np.array([1,2,3]) , b=np.array([4,5,6])

# In[23]:


a=np.array([1,2,3]) 
b=np.array([4,5,6])
print(np.concatenate((a,b)))


# 8.Create a dataframe with 3 rows and 2 columns

# In[24]:


import pandas as pd


# In[28]:


r=[1,2,3]
c=['a','b']
data=np.random.randint(10,size=(3,2))
df=pd.DataFrame(data,index=r,columns=c)
print(df)


# 9.Generate the series of dates from 1st Jan 2023 to 10th Feb 2023

# In[29]:


pd.date_range(start="2023-01-01",end="2023-02-10")


# 10.Create 2D list to DataFrame?

# In[30]:


lists = [[1,'aaa', 22], [2,'bbb', 25], [3,'ccc', 24]] 
df = pd.DataFrame(lists, columns =['Token', 'ID','value']) 
print(df )


# In[ ]:




