#!/usr/bin/env python
# coding: utf-8

# In[87]:


import numpy as np

x = np.array([1, 2, 3])
for i in x:
    print(i)


# In[88]:


import numpy as np

x = np.array([[1, 2, 3],[4, 5, 6]])

for i in x:
    print(i)


# In[89]:


import numpy as np

x =np.array([[1, 2, 3],[4, 5, 6]])

for y in x:
    for z in y:
        print(z)


# In[91]:


import numpy as np

x = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])

for i in np.nditer(x):
    print(i)

