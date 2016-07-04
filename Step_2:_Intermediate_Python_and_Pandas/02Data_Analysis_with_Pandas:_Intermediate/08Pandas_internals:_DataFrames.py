#coding: UTF-8
import numpy as np
import pandas as pd

fandango = pd.read_csv("fandango_score_comparison.csv")
#print(fandango.head(2))
print(fandango.index)
print(fandango.columns)

#Selecting Using Integer index
#We can use the integer index to select rows a few different ways:
#When selecting an individual row, Pandas will return a Series object. When selecting multiple rows, a DataFrame that is a subset of the original DataFrame will be returned.
print(fandango[0:2])
print(fandango[144:])
#to select individual row,nedd to use iloc[] method.
print(fandango.iloc[50])
print(fandango.loc[[45,90]])

#custom index
#The DataFrame object contains a set_index() method that allows you to pass in the name of the column you'd like Pandas to use as the index for the DataFrame.
#set_index() contains a few parameters below;
#    inplace: if set to True, will set the index to the current DataFrame instead of returning a new one
#    drop: if set to False, will keep the column you specified for the index in the DataFrame

fandango_films = fandango.set_index("FILM",drop=False)
#print(fandango_films.index)

#Apply over columns
#The apply() method requires you to pass in a vectorized operation that can be applied over each Series object.
#By default, the method runs over the DataFrame's columns
types = fandango_films.dtypes #return the data types as a series
print(types)
float_columns = types[types.values == 'float64'].index
print(float_columns)
float_df = fandango_films[float_columns] #use bracket notation to filter columns to just float columns

deviations = float_df.apply(lambda x: np.std(x)) # `x` is a Series object representing a column
print(deviations)

#Apply() over rows
#To apply a function over the rows (each row will be treated as a Series object) in a DataFrame,
#we need to set the axis parameter to 1 after we specify the function we want to apply.
rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
rt_mt_deviations = rt_mt_user.apply(lambda x: np.mean(x), axis=1)
print(rt_mt_deviations)
