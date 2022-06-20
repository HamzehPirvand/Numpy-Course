#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7])
print(x[1:5])


# In[62]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7])
print(x[4:])


# In[63]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7])
print(x[:4])


# In[64]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7])
print(x[-3:-1])


# In[65]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7])
print(x[1:5:2])


# In[66]:


import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7])
print(x[::2])


# In[67]:


import numpy as np

x = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(x[1, 1:4])


# In[68]:


import numpy as np

x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(x[0:2, 2])


# In[69]:


import numpy as np

x = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(x[0:2, 1:4])

