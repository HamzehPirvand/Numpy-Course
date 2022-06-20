#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array_split(x, 3)

print(y)


# In[2]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array_split(x, 3)

print(y[0])
print(y[1])
print(y[2])


# In[3]:


import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
y = np.array_split(x, 3)

print(y)


# In[5]:


import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
y = np.array_split(y, 3)

print(y)


# In[7]:


import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
y = np.array_split(x, 3, axis=1)

print(y)


# In[8]:


import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
y = np.hsplit(x, 3)

print(y)

