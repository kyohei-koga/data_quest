#coding: UTF-8

import numpy as np
import pandas as pd

#Data structure
#The three key data structures in Pandas are:
#    -Series (collection of values)
#    -DataFrame (collection of Series objects)
#    -Panel (collection of DataFrame objects)

fandango = pd.read_csv("fandango_score_comparison.csv")
print(fandango.columns)

#Integer index
print(fandango["RottenTomatoes"][0:5])#series object can use directly slice, correspond to dataframe object using .iloc or .loc

#Custom index
#for using string index create new series object which have string index.
series_film = fandango["FILM"]
series_rt = fandango["RottenTomatoes"]
film_names = series_film.values #convert to array-like object
rt_scores = series_rt.values
series_custom = pd.Series(data=rt_scores,index=film_names) #create new series object has string index.
print(series_custom[["Minions(2015)","Leviathan(2014)","Cinderella (2015)"]])

#Integer index preserved
#Even though we specified that the series object uses a custom, the object still maintain an important integer index we can use for selection.
print(series_custom[5:10])

#Reindexing
original_index = series_custom.index.tolist() #convert to list object
sorted_index = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted(original_index)) #sort series object in alphabetical order, and then reindex

#Sorting
#sorting by reindexing can cumbersome if we want to order by other contents.
#To make sorting easier, Padas comes with a sort_index() method, which returns a Series sorted by the index.
#sort_values() method, which returns a Series sorted by the value.
sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()

#Vectorized Operation
#The values in a Series object are treated as an ndarray, the core data type in NumPy.
#Applying some NumPy functions will return a new Series object while others will return just a single value.
#NumPy's documentation gives you a good sense of the return value for each function.
#If a particular NumPy function usually returns an ndarray, it will instead return a Series object when applied to a Series.
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.sin.html#numpy.sin

#Alignment
# For DataFrame objects, the values are linked to the index labels and the column labels,
#and are also preserved unless we explicitly break the link (by reassigning or editing a column or index label, for example)
#This core tenet allows us to use Pandas effectively when working with data and is a big advantages over just using NumPy objects.
rt_critics = pd.Series(fandango["RottenTomatoes"].values, index=fandango["FILM"]) #first parameter is "data"
rt_users = pd.Series(fandango["RottenTomatoes_User"], index=fandango["FILM"])
rt_mean = (rt_critics + rt_users) / 2
rt_mean_sort = rt_mean.sort_values()
