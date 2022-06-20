#!/usr/bin/env python
# coding: utf-8

# In[70]:


import numpy as np

x = np.array([1, 2, 3, 4])
print(x.dtype)


# In[71]:


import numpy as np

x = np.array(["apple", "kiwi", "mango"])
print(x.dtype)


# In[73]:


import numpy as np

x = np.array([1, 2, 3, 4], dtype="S")
print(x.dtype)
print(x)


# In[74]:


import numpy as np

x = np.array([1, 2, 3, 4], dtype="i4")
print(x)
print(x.dtype)

