#!/usr/bin/env python
# coding: utf-8

# In[41]:


x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
    z.append(i + j)
print(z)


# In[42]:


x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)


# In[43]:


import numpy as np

def myadd(x, y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))


# In[44]:


import numpy as np

print(type(np.add))


# In[46]:


import numpy as np

print(type(np.concatenate))


# In[47]:


import numpy as np

if type(np.add) == np.ufunc:
    print("add is ufunc")
else:
    print("add is not ufunc")


# In[48]:


import numpy as np

x = np.array([10, 11, 12, 13, 14, 15])
y = np.array([20, 21, 22, 23, 24, 25])

z = np.add(x, y)
print(z)


# In[49]:


import numpy as np

x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([20, 21, 22, 23, 24, 25])

z = np.subtract(x, y)
print(z)


# In[50]:


import numpy as np

x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([20, 21, 22, 23, 24, 25])

z = np.multiply(x, y)
print(z)


# In[51]:


import numpy as np

x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([3, 5, 10, 8, 2, 33])

z = np.divide(x, y)
print(z)


# In[52]:


import numpy as np

x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([3, 5, 6, 8, 2, 33])

z = np.power(x, y)
print(z)


# In[53]:


import numpy as np

x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([3, 7, 9, 8, 2, 33])

z = np.mod(x, y)
print(z)


# In[55]:


import numpy as np

x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([3, 7, 9, 8, 2, 33])

z = np.remainder(x, y)
print(z)


# In[56]:


import numpy as np

x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([3, 7, 9, 8, 2, 33])

z = np.divmod(x, y)
print(z)


# In[57]:


import numpy as np

x = np.array([-1, -2, 1, 2, 3, -4])

y = np.absolute(x)
print(y)

