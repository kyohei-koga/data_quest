#coding: UTF-8

import pandas
food_info = pandas.read_csv("food_info.csv")
cols = food_info.columns.tolist
print(cols)
print(food_info.head(3))

#Transforming a column
#I can use the arithmetic operators to transform individual columns.
test_div_100 = food_info['Protein_(g)'] / 100
print(test_div_100.iloc[0:3])
food_info[food_info["Water_(g)"]=="--"] = "0"
food_info[food_info["Energ_Kcal"]=="--"] = "0"
water = food_info["Water_(g)"].astype(float)
energy = food_info["Energ_Kcal"].astype(float)
water_energy = water * energy
print(water_energy.iloc[0:3])

#Normalizing columns
#one of the simplest way is to divide all of the values in a column by that column's maximum value.
normalized_water = water / water.max()
print(normalized_water.iloc[0:3])

#Creating new column
food_info["Normalized_water"] = normalized_water
print(food_info.columns)

#Soerting a DataFrame by a column
#DataFrame objects contain a sort() method that we can use to sort the entire DataFrame by.
#documentation URL below.
#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort.html
food_info.sort("Water_(g)",inplace=False,ascending=False)
print(food_info["Water_(g)"].head(3))
