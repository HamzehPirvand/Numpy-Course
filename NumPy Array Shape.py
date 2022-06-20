#!/usr/bin/env python
# coding: utf-8

# In[80]:


import numpy as np

x = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(x.shape)


# In[81]:


import numpy as np

x = np.array([1, 2, 3, 4, 5], ndmin=5)

print(x)
print("shape of array : ", x.shape)

