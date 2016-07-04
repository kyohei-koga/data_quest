#coding: UTF-8
import pandas as pd
import numpy as np

#In this mission, we'll work on cleaning up and analyzing data on passenger survival from the Titanic.

#Finding the missing data
#In Python there is None kyeword and type, which indicates no value.
#Pandas uses NaN, which stands for "not a number", to indicate a missing value.
#We can also call NaN a null value.
titanic_survival = pd.read_csv("titanic_survival.csv")
print(titanic_survival.dtypes)
print(titanic_survival.columns)
age_null = pd.isnull(titanic_survival["Age"]) #isnull function find which values in a column are missing.
age_null_count = 0
for row in age_null:
    if row:
        age_null_count += 1
print(age_null_count)

#Whats the big deal with missing data?
#What we have to do instead is filter the missing values out before we compute the mean
good_age = titanic_survival["Age"][age_null == False]
correct_mean_age = sum(good_age) / len(good_age)
print("mean age is %s") %correct_mean_age

#easier way to do math
#we can use the .mean() method to do compute the ean, and it will automatically remove missing values.
correct_mean_age = titanic_survival["Age"].mean()
correct_mean_fare = titanic_survival["Fare"].mean()
print("mean fare is %s") %correct_mean_fare

#computing sumary statistics
passenger_classes = [1,2,3]
fare_by_class = {}

for row in passenger_classes:
    fare_for_class = titanic_survival["Fare"][titanic_survival["Pclass"] == row]
    fare_by_class[row] = fare_for_class.mean()
print(fare_by_class)

#Making pivot tables
#the pivot_table method on a pandas dataframe will let us do this.
#index specifies which columns to subset data based on.
#values specifies which column to subset based on the index
#The aggfunc specifies what to do with the subsets.
passenger_survival = titanic_survival.pivot_table(index="Pclass",values="Survived",aggfunc=np.mean)
passenger_age = titanic_survival.pivot_table(index="Age",values="Survived",aggfunc=np.mean)
print(passenger_survival)

#More complex pivot tables
#We can make more complex pivot tables that show multiple values at onces.
passenger_survival = titanic_survival.pivot_table(index="Pclass",values=["Age","Survived"],aggfunc=np.mean)
print(passenger_survival)

#Drop missing values
#We can use the dropna method on Pandas dataframe to remove missing values in a matrix

#Drop all rows that have missing values
new_titanic_survival = titanic_survival.dropna()
#but it looks like we have a fewer dataframe now.
#This is because every row has many missing value.
#print(new_titanic_survival)

#we can use the subset argument to only drop rows if certain columns have missing values.
new_titanic_survival = titanic_survival.dropna(subset=["Age","Sex"])
#print(new_titanic_survival)

#Row indices
#we've been using the .iloc method to address rows and columns
#.iloc method works by position (row/colmun number)
#The below code prints the fourth row in the data
print(new_titanic_survival.iloc[4,:])

#using .loc instead addresses rows and columns by index, not position.
#This actually prints the first row, because it has index 3
print(new_titanic_survival.loc[3,:])
print("\n")
print(new_titanic_survival.loc[3,"Pclass"])

#Reindex rows
#new_titanic_survival did'nt have sequetial row indexes.
#Each row retain its original index from titanic_survival.
#sometimes it is useful to reindex, and make new indeces starting from 0.
#To do this, we can use the reset_index() method.

#The drop keyword argument specifies wheather or not to make a dataframe column with the index values.
new_titanic_survival = new_titanic_survival.reset_index(drop=True)
#print(new_titanic_survival)

#Use the apply function
#By default, apply() will iterate through each column in a dataframe, and perform a function on it.
#The result from the function will be combined with all of the other result, and placed into a new series.

#This function counts the number of null values in a series.
def null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null == True]
    return len(null)
#compute null counts for each column
column_null_count = titanic_survival.apply(null_count)
print(column_null_count)

#Applying a function to a row
#By passing the axis argument, we can use the .apply() method to iterate over rows instead of columns
#This function will check if a row is an entry for a minor (under 18), or more
def is_minor(row):
    if row["Age"] < 18:
        return True
    else:
        return False

#Each entry is True if the row at the same position is a record for a minor.
#The axis of 1 specifies that it will iterate over rows, not column
minors = titanic_survival.apply(is_minor,axis=1)
#print(minors)

#practice
#create age_label

def func(row):
    if row["Age"] < 18:
        return "minor"
    elif row["Age"] >= 18:
        return "adult"
    elif pd.isnull(row["Age"]):
        return "unknown"

age_label = titanic_survival.apply(func,axis=1)
#print(age_label)
#Creating new column
titanic_survival["Age_label"] = age_label
print(titanic_survival.dtypes)

#computing survival percentage y age group
age_group_survival = titanic_survival.pivot_table(index="Age_label",values="Survived",aggfunc=np.mean)
print(age_group_survival)
