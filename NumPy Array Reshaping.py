#!/usr/bin/env python
# coding: utf-8

# In[82]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = x.reshape(4, 3)

print(y)


# In[83]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = x.reshape(2, 3, 2)

print(y)


# In[85]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(x.reshape(2, 4).base)


# In[86]:


import numpy as np

x = np.array([[1, 2, 3],[4, 5, 6]])
y = x.reshape(-1)

print(y)

