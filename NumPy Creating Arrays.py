#!/usr/bin/env python
# coding: utf-8

# In[46]:


import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(x)


# In[47]:


import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(type(x))


# In[48]:


import numpy as np

x = np.array(45)
print(x)


# In[50]:


import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)


# In[51]:


import numpy as np

x = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
print(x)


# In[52]:


import numpy as np

a = np.array(45)
b = np.array([1, 2, 3])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# In[55]:


import numpy as np

x = np.array([1, 2, 3, 4], ndmin = 5)

print(x)
print("number of dimension :", x.ndim)


# In[ ]:




