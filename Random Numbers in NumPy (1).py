#!/usr/bin/env python
# coding: utf-8

# In[33]:


from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)


# In[34]:


from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)


# In[35]:


from numpy import random
import numpy as np

x = np.array([1, 2, 3, 4, 5])
random.shuffle(x)

print(x)


# In[36]:


from numpy import random
import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(random.permutation(x))


# In[ ]:




