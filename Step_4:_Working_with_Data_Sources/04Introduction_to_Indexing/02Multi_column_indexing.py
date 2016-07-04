
# coding: utf-8

# # Introduction
# In this mission, we'll explore how to create indexes for speeding up queries that filter on multiple columns.

# In[19]:

import sqlite3
conn = sqlite3.connect("factbook.db")
cur = conn.cursor()
query = "explain query plan select * from facts where (population > 1000000) and (population_growth < 0.05);"
query_plan_one = cur.execute(query).fetchall()
print(query_plan_one)


# # Query plan for multi-column queries

# In[26]:

cur.execute("create index if not exists pop_idx on facts(population);")
cur.execute("create index if not exists pop_growth_idx on facts(population_growth);")

query = "explain query plan select * from facts where (population > 1000000) and (population_growth < 0.05);"
query_plan_two = cur.execute(query).fetchall()
print query_plan_two


# # Creating a multi-column index
# To create a multi-column index, we use the same CREATE INDEX syntax as before but instead specify 2 columns in the ON statement

# In[27]:

query = "create index if not exists pop_pop_growth_idx on facts(population,population_growth);"
conn.execute(query)
query_plan_three = conn.execute("explain query plan select * from facts where (population > 1000000) and (population_growth < 0.05)")
print(query_plan_three)


# # Covering index

# In[28]:

conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")
query_plan_four = conn.execute("explain query plan select population, population_growth from facts where population > 1000000 and population_growth < 0.05;").fetchall()
print(query_plan_four)


# # Covering index for single column
# Even though the query plan indicates that a binary search on facts was performed, this is misleading and it was instead able to use the covering index. You can read more about that on the documentation.
# 
# Covering indexes don't apply just to multi-column indexes. If a query we write only touches a column in the database that we have a single-column index for, SQLite will use only the index to service the query. 
# 

# In[29]:

conn = sqlite3.connect("factbook.db")
conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")
query_plan_five = conn.execute("explain query plan select population from facts where population > 1000000;").fetchall()
print(query_plan_five)


# In[ ]:



