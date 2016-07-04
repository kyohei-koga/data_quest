#coding: UTF-8

#One of the biggest advantages that Pandas has over NumPy is the ability to store mixed data types in rows and columns.
#we use the Pandas method read_csv() to read a csv file
import pandas
food_info = pandas.read_csv("food_info.csv")
print(type(food_info))

#Exploring the DataFrame
#call head() method, Pandas will return a new DataFrame contraining just 5 rows
#To access the full list of column names, use the columns attribute
#To understand the dimensions of DataFrame, use shape attribute
print(food_info.head(3))
print(food_info.columns)
print(food_info.shape)

#Series
#The main advantage of series object is the aility to utilize a non-integer labels.
#Numpy arrays can only utilize integer labels for indexing.

#Selecting a row
#we need to use the Pandas method loc[] to select rows in a DataFrame.
first_row = food_info.loc[0]
hundredth_row = food_info.loc[99]
print(first_row,hundredth_row)

#Data types
print(food_info.dtypes)

#Selecting individual columns
#To access a single column, use bracket notation and pas in the column name as a string.
ndb_col = food_info['NDO_No']
cholestrl = food_info['Cholestrl_(mg)']
print(type(ndb_col))

#Selecting multiple columns by name
columns = ['Shrt_Desc','Water_(g)']
name_and_water = food_info[columns]
print(name_and_water.head(2))


#Practice
columns_name = food_info.columns
columns_name_list = columns_name.tolist() #use columns attribute tolist() to convert to a list
gram_columns = []
for row in columns_name_list:
    if row.endswith("(g)"):  #the string method endwith return True if the string object calling the method ends with the string passed into the parentheses.
        gram_columns.append(row)
gram_df = food_info[gram_columns]
print(gram_df.head(3))
