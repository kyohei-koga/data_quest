#coding: UTF-8

#Darabase
#As the data gets larger, it becomes more difficult to load the file into a computer's memory, which is how tools like Pandas work with data.
import sqlite3

#SQLite is a database that doesn't require a standalone server process and stores the entire database as a file on disk.
#This makes it ideal for working with larger datasets that can fit on disk but not in memory.

#Connect To The DataBase
#we connect to the database we want to query using the connect() function.
#The connect() function has a single required parameter, the database we want to connect to.
#Since the database we're working with is stored as a file on disk, we need to pass in the filename.
#When you're connected to a database, SQLite locks the database file and prevents any other process
#from connecting to the database simultaneously.

conn = sqlite3.connect("jobs.db")

#Tuples
#A tuple is a core Python data structure used to represent a sequence of values, similar to a list.
#Unlike lists, tuples are immutable, which means they can't be modified after creation.


#Running a query
#We need to use the Connection instance method cursor() to return a Cursor instance corresponding to the database we want to query.
cursor = conn.cursor()

query = "select * from recent_grads" #SQL
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])


#Fetching a specific number of results
#we use the Cursor method fetchone() and to return n results, we use the Cursor method fetchmany()
#You will notice that fetch method slide the reference row No.
#So if you use fetchall first, you can't get any information same table by any fetch method after that.

first_result = cursor.fetchone()
second_result = cursor.fetchone()
five_results = cursor.fetchmany(5)

print(first_result)
print(second_result)
print(five_results)

#Closing the connecttaquest

#losing the connection to the database allows other processes to access the database,
#which is important when you're in a production environment and working with other team members.
conn = sqlite3.connect("jobs.db")
query = "select Major from recent_grads order by Major desc;"
#reverse_alphabetical
conn.close()
