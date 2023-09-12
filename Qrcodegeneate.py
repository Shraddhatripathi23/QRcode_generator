#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install qrcode


# In[2]:


import qrcode
img = qrcode.make("https://shraddha-tripathi.netlify.app/")
img.save ("shraddha.jpg")


# In[ ]:




