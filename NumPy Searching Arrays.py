#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 4, 4])
y = np.where(x == 4)

print(y)


# In[13]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.where(x%2 == 0)

print(y)


# In[14]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.where(x%2 == 1)

print(y)


# In[15]:


import numpy as np

x = np.array([6, 7, 8, 9])
y = np.searchsorted(x, 7)

print(y)


# In[16]:


import numpy as np

x = np.array([6, 7, 8, 9])
y = np.searchsorted(x, 7, side="right")

print(y)


# In[18]:


import numpy as np

x = np.array([1, 3, 5, 7])
y = np.searchsorted(x, [2, 4, 6])

print(y)

