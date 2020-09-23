#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')
from mpl_toolkits.mplot3d import Axes3D
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.scatter(x,y, marker = '*', s= 50)
plt.title('Orion constellation 2D')

plt.show()


# In[59]:


fig_3d = plt.figure()
fig3d = fig_3d.add_subplot(1,1,1, projection='3d')
fig3d.scatter(x,y,z, color = 'orange', marker = '*', s=50)
fig3d.w_xaxis.set_pane_color((0.7, 0.9, 0.9, 1.0))
fig3d.w_yaxis.set_pane_color((0.7, 0.9, 0.9, 1.0))
fig3d.w_zaxis.set_pane_color((0.7, 0.8, 0.8, 1.0))
fig3d.grid(False)
plt.show()


# In[ ]:





# In[ ]:




