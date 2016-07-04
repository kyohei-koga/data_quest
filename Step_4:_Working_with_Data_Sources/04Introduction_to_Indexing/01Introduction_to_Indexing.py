
# coding: utf-8

# In[1]:

import sqlite3
conn = sqlite3.connect("factbook.db")
cur = conn.cursor()
query = "pragma table_info(facts)"
cur.execute(query)
schema = cur.fetchall()
for row in schema:
    print row


# # Query planner
# If the parser was able to successfully parse the query, then SQLite moves on to the query planning and optimization phase.
# 
# There are many different ways for SQLite to access the underlying data in a database. 
# 
#  The query optimizer generates cost estimates for the various ways to access the underlying data, factoring in the schema of the tables and the operations the query requires. The heuristics and algorithms that are involved in query optimization is complex and out of this mission's scope.
#  
#  The optimizer quickly assesses the various ways to access the data and generates a best guess for the fastest query plan. 

# # Explain query plan
# We can use the EXPLAIN QUERY PLAN statement before any query we're running to get a high level query plan that would be performed. 
# 
# We'll focus on the value at index 4 in the returned tuple in this mission. SCAN TABLE means that every row in entire table (facts) had to be accessed to evaluate the query.

# In[3]:

query = "explain query plan select * from facts where area>40000;"
query_plan_one = cur.execute(query).fetchall()
print query_plan_one


# # Data representation
# Even though the queries asked for a subset of the facts table, SQLite still ends up scanning the entire table.This is because of the way SQLite represents data. 
# 
# Since the rows are ordered by id, SQLite can search for a specific row based on it's id value using binary search.
# 
# Unless we provide specific id values in the WHERE statement in the query, SQLite can't take advantage of binary search and has to instead scan the entire table, row by row.

# # Time complexity
# Binary search on a table using the primary key would be O(log N) time complexity where N is the number of total rows in the table. 

# In[6]:

query = "explain query plan select * from facts where id == 20;"
query_plan_four = conn.execute(query).fetchall()
print query_plan_four


# # Search and rowid
# SQLite uses rowid to refer to the primary key of a table. The alias rowid will be displayed in the query plan, no matter what you name the primary key column for that table. 

# # Indexing
# SQLite can take advantage of speedy lookups when searching for a specific primary key. 
# We need a way to take advantage of the speed that lookups by primary keys give us without knowing the primary key when querying. To accomplish that, we could create a separate table that's optimized for lookups on a specific value in a column from the facts table instead of by the id. We call this table an index and each row in the index contains

# # All together now

# In[9]:

query_plan_six = conn.execute("explain query plan select * from facts where population > 10000;")
print query_plan_six

conn.execute("create index if not exists pop_idx on facts(population)")
query_plan_seven = conn.execute("explain query plan select * from facts where population > 10000 ;").fetchall()
print(query_plan_seven)


# In[ ]:



