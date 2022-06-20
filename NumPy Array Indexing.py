#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(x[2])


# In[57]:


import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(x[2] + x[3])


# In[58]:


import numpy as np

x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2nd elementon 1st list dim: ", x[0, 1])


# In[59]:


import numpy as np

x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("4th element on 2nd dim: ", x[1, 4])


# In[60]:


import numpy as np

x = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(x[0, 1, 2])

