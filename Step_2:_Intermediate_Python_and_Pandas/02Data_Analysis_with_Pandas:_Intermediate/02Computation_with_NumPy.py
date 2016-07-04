#coding: UTF-8

#Array comparison
#One of the most powerful aspects of NumPy is the ability to make comparison across an entire array.
import numpy as np
#f = open(world_alcohol.csv,r)
world_alcohol = np.genfromtxt("world_alcohol.csv",delimiter=",",dtype="string")
print(world_alcohol[0,:])
countries_canada = (world_alcohol[:,5] == 'Canada')
years_1894 = (world_alcohol[:,3] == '1984')
#print(countries_canada)


#Selecting elements by using Array compariosn stated above.
country_is_algeria = (world_alcohol[:,5] == 'Jamaica')
country_algeria = world_alcohol[country_is_algeria,:]
#print(country_algeria)

#Comparisons with multiple conditions
is_algeria_and_1986 = (world_alcohol[:,3] == '1986') & (world_alcohol[:,5] == 'Algeria')
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

#Replacing enpty strings
#Before we can convert the column to floats, we have to deal with empty string values ('').
is_value_empty = (world_alcohol[:,7] == '') | (world_alcohol[:,7] == 'No data')
world_alcohol[is_value_empty,7] = '0'

#Converting data type
#We can convert the data type of an array using the astype() method.
alcohol_consumption = world_alcohol[1:,7]
print(alcohol_consumption[:1].astype(float))
try:
    alcohol_consumption = alcohol_consumption.astype(float) #convert string to float
except Exception as exc:
    print(str(exc))

print(alcohol_consumption)

#Computing with Numpy
#buit in method is beloe URL
#http://docs.scipy.org/doc/numpy-1.10.1/index.html
total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()
max_alcohol = alcohol_consumption.max()

print("sum = %s\naverage = %s\nmax = %s") %(total_alcohol,average_alcohol,max_alcohol)

is_canada_1986 = (world_alcohol[:,5] == 'Canada') & (world_alcohol[:,3] == '1979')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = canada_1986[:,7]
empty_strings = canada_alcohol == ''
canada_alcohol[empty_strings] = '0'
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()
print("total canadian drinking = %s") %total_canadian_drinking

countries = set(world_alcohol[:,5])

totals = {}
is_1989 = world_alcohol[:,3] == '1977'
year = world_alcohol[is_1989,:]

for country in countries:
    is_country = (year[:,5] == country)
    country_consumption = year[is_country,7]
    is_empty = (country_consumption[:] == '') | (country_consumption[:] == 'No data')
    country_consumption[is_empty] = '0'
    country_consumption = country_consumption.astype(float)
    totals[country] = country_consumption.sum()
#print(totals)

highest_value = 0
highest_key = None

for country in totals:
    if totals[country] > highest_value:
        highest_value = totals[country]
        highest_key = country
print("%s is highest total alcohol consumption country,and total consumption is %s")%(highest_key, highest_value)

#Numpy has two limitations
#1. A whole array has to be the same datatype, which makes it cumbersome to work with many datasets
#2. columns and rows have to be referred to by number, which gets confusing when you go back and forth column name to column number.
