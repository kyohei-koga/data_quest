
# coding: utf-8

# In[3]:

import sqlite3
conn = sqlite3.connect("factbook.db")
cur = conn.cursor()
query = "select * from facts;"
cur.execute(query)
facts = cur.fetchall()
facts_count = len(facts)
facts_count


# # Counting in SQL
# Thankfully, SQL includes the COUNT aggregation function, which allows us to count the number of records in a table.

# In[5]:

query = "select count(*) from facts;" #count the number of rows in the facts table of factbook.db
cur.execute(query)
result = cur.fetchall()
print result


# In[8]:

#only count the total number of non-null values in the area_water column
query = "select count(birth_rate) from facts;" 
cur.execute(query)
result = cur.fetchall()
print result


# # Min and max in SQL

# In[10]:

query = "select min(population_growth) from facts;"
cur.execute(query)
result = cur.fetchall()
print result

query = "select max(death_rate) from facts"
cur.execute(query)
result = cur.fetchall()
print result


# # Sum and average in SQL

# In[11]:

query = "select sum(area_land) from facts;"
cur.execute(query)
result = cur.fetchall()
print result

query = "select avg(area_water) from facts;"
cur.execute(query)
result = cur.fetchall()
print result


# # Multiple aggregation functions
# If we wanted to use the SUM, AVG, and MAX functions on a column, it would be inefficient to write three different queries to retrieve the information. You may recall that we can query multiple columns by separating the names with a comma

# In[12]:

query = "select avg(population),sum(population),max(birth_rate) from facts"
cur.execute(query)
result = cur.fetchall()
print result


# # Conditional aggregation
# As you may recall from earlier, we can use the WHERE statement to only query certain rows in a SQL table

# In[13]:

query = "select avg(population_growth) from facts where population > 10000000"
cur.execute(query)
result = cur.fetchall()
print result


# # Selecting unique rows
# There are cases when we'll only want to select the unique values in a column or database, and not get each individual row. One example is if our facts table had duplicate entries for each country
# 
# If we want to get a list of all the countries in the world, we'll need to remove these duplicate rows, so countries appear twice. We can do this with the DISTINCT statement
# 
# The above query will select unique pairs of population and name values from facts

# In[14]:

query = "select distinct birth_rate from facts;"
cur.execute(query)
unique_birth_rates = cur.fetchall()
print unique_birth_rates


# # Distinct aggregations
# If we wanted to count the number of unique items in the population column, we could use the COUNT aggregation function along with the DISTINCT statement. Here's how it would work

# In[15]:

query = "select avg(distinct birth_rate) from facts where population > 20000000"
cur.execute(query)
result = cur.fetchall()
print(result)


# # Arithmetic in SQL

# In[18]:

query = "select population_growth / 1000000.0 from facts"
cur.execute(query)
population_growth_millions = cur.fetchall()
print 


# # Arithmetic between columns

# In[19]:

query = "select (population * population_growth) + population from facts;"
cur.execute(query)
next_year_population = cur.fetchall()
print(next_year_population)


# In[ ]:



