#!/usr/bin/env python
# coding: utf-8

# In[24]:


from numpy import random

x = random.randint(100)

print(x)


# In[26]:


from numpy import random

x = random.rand()
print(x)


# In[27]:


from numpy import random

x = random.randint(100, size=(5))
print(x)


# In[28]:


from numpy import random

x = random.randint(100, size=(3, 5))
print(x)


# In[29]:


from numpy import random

x = random.rand(5)
print(x)


# In[30]:


from numpy import random

x = random.rand(3, 5)
print(x)


# In[31]:


from numpy import random

x = random.choice([3, 5, 7, 9])
print(x)


# In[32]:


from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

