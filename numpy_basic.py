#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy


x = numpy.array([11, 22, 33, 44, 55])

print(x)


# In[2]:


import numpy as np

y = np.array([100, 200, 300, 400, 500])

print(y)


# In[3]:


print(np.__version__)


# In[4]:


z = np.array((44, 55, 66, 77, 88, 99, 11))

print(z)


# In[5]:


# TWO DI ARRAY


# In[6]:


x1 = np.array([[1, 2, 3, 4, 5], [11, 22, 33, 44, 55]])

print(x1)
print(x1.ndim)


# In[7]:


# THREE DI ARRAY


# In[8]:


y1 = np.array([[[[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [3, 13, 23, 33, 43, 53]]]])

print(y1.ndim)


# In[9]:


z1 = np.array(56)

print(z1)


# In[10]:


# ARRAY DI CHECK


# In[11]:


print(z1.ndim)


# In[12]:


print(x1.ndim)


# In[13]:


print(y1.ndim)


# In[14]:


q1 = np.array([[[1,2,3], [9,8,7], [66,88,77], [65, 45, 55]]])

print(q1)

print(q1.ndim)


# In[15]:


one = np.array([10,20,30,40,50])

print(one)
print(one.ndim)

print(one[3])


# In[16]:


two = np.array([[2,4,6,8,10], [10,20,30,40,50]])

print(two)
print(two.ndim)
# two[0, 2]: 0 is first dimention il 2 is second element
print(two[0, 2])
print(two[1, 3])


# In[25]:


# [[[10,20,30,40], [50,60,70,80]]]
three = np.array([[[10,20,30,40], [1,2,3,4], [45, 55, 65, 75], [75,85,95,105]]])

print(three)
print(three.ndim)
# 
# [oth array, 2nd list, 3rd position]
print(three[0, 2, 3])
print(three[0, 3, 2])


# In[ ]:




