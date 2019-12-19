#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as n
from scipy import stats

import matplotlib
import matplotlib.pyplot as plt


# In[30]:


get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.style.use('ggplot')

#n.random.seed(1)

data = [5.2,3.2,5.7,6.9,2.8,3.5,6.7,7.8,7.3,7.2,9.5,4.5,4.2,2.8,3.2,4.9,5.9,9.2,5.7,4.5]
print("1d array values..\n",data);

plt.hist(data, bins=10, range=(0,10), edgecolor='black')
plt.show()


# In[31]:


mean = n.mean(data)
mean


# In[9]:


n.median(data)


# In[14]:


mode = stats.mode(data)
#print("mode : ",mode)
print("The modal value is {} with a count of {}".format(mode.mode[0], mode.count[0]))


# In[32]:


n.ptp(data)


# In[16]:


n.var(data)


# In[17]:


n.std(data)


# In[18]:


stats.sem(data)


# In[ ]:




