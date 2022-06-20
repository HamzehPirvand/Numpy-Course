#!/usr/bin/env python
# coding: utf-8

# In[77]:


import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = x.view()
x[3] = 90

print(x)
print(y)


# In[78]:


import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = x.copy()
x[1] = 37

print(x)
print(y)


# In[79]:


import numpy as np

x = np.array([1, 2, 3, 4, 5])

y =  x.copy()
z = x.view()

print(y.base)
print(z.base)

