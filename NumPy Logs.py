#!/usr/bin/env python
# coding: utf-8

# In[63]:


import numpy as np

x = np.arange(1, 10)
print(x)


# In[64]:


import  numpy as np

x = np.arange(1, 10)
print(np.log10(x))


# In[65]:


import numpy as np

x = np.arange(1, 10)
print(np.log(x))


# In[66]:


import numpy as np

x = np.array([1, 2, 3])
y = np.array([1, 2, 3])

z = np.sum([x, y], axis=1)
print(z)


# In[67]:


import numpy as np

x = np.array([1, 2, 3])

y = np.cumsum(x)
print(y)


# In[68]:


import numpy as np

x = np.array([1, 2, 3, 4])
y = np.prod(x)

print(y)


# In[69]:


import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])

z = np.prod([x, y])
print(z)


# In[70]:


import numpy as np

x = np.array([5, 6, 7, 8])
y = np.cumprod(x)

print(y)


# In[71]:


import numpy as np

x = np.array([10, 15, 25, 5])
y = np.diff(x)

print(y)


# In[73]:


import numpy as np

x = np.array([10, 15, 25, 5])
y = np.diff(x, n=2)

print(y)


# In[74]:


import numpy as np

x = 6
y = 4

z = np.lcm(x, y)
print(z)


# In[75]:


import numpy as np

x = np.array([3, 6, 9])
y = np.lcm.reduce(x)

print(y)


# In[76]:


import numpy as np

x = 6
y = 9

z = np.gcd(x, y)
print(z)


# In[77]:


import numpy as np

x = np.array([20, 8, 32, 36, 16])
y = np.gcd.reduce(x)

print(y)


# In[78]:


import numpy as np

x = np.sin(np.pi/2)

print(x)


# In[79]:


import numpy as np

x = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
y = np.sin(x)

print(y)


# In[80]:


import numpy as np

x = np.array([90, 180, 270, 360])
y = np.deg2rad(x)

print(y)


# In[81]:


import numpy as np

x = np.arcsin(1.0)
print(x)


# In[82]:


import numpy as np

x = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

y = np.cosh(x)
print(y)


# In[83]:


import numpy as np

x = np.arcsinh(1.0)
print(x)


# In[84]:


import numpy as np

x = np.array([0.1, 0.2, 0.5])
y = np.arctanh(x)

print(y)

