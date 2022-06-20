#!/usr/bin/env python
# coding: utf-8

# In[92]:


import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

z = np.concatenate((x, y))
print(z)


# In[93]:


import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

z = np.stack((x, y), axis=1)
print(z)


# In[94]:


import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

z = np.hstack((x, y))
print(z)


# In[95]:


import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

z =np.vstack((x, y))
print(z)


# In[96]:


import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

z = np.dstack((x, y))
print(z)

