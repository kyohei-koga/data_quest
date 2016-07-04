
# coding: utf-8

# In[1]:

import sqlite3


# In[3]:

con = sqlite3.connect("factbook.db")
# We then create a Cursor instance, which can execute queries. 
cur = con.cursor()


# In[4]:

query = "select sum(area_land) from facts;"
cur.execute(query)
a = cur.fetchall()


# In[7]:

query2 = "select sum(area_water) from facts;"
cur.execute(query2)
b = cur.fetchall()
print(a[0][0])
c = float(a[0][0]) / float(b[0][0])
print(c)


# In[ ]:



