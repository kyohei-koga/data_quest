
# coding: utf-8

# In[1]:

#You can read the results of a SQL query into a Pandas Dataframe using the read_sql_query function.
import pandas as pd
import sqlite3
import math


# In[2]:

conn = sqlite3.connect("factbook.db")
cur  = conn.cursor()


# In[3]:

sql = "select * from facts;"
facts = pd.read_sql_query(sql,conn)
facts.dropna(axis=0)


# In[4]:

def population_growth(initial_population,growth_rate):
    return initial_population * math.e **(growth_rate*35)


# In[6]:

facts["35years_later"] = facts.apply(lambda x:population_growth(x["population"],x["population_growth"]),axis=1)
print(facts.sort_values(by="35years_later",ascending=False)[["name","35years_later"]].head(10))


# In[ ]:



