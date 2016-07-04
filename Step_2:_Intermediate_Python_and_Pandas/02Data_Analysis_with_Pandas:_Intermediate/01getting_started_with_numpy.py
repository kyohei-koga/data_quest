#coding: UTF-8
#the conventional way of caluculatig average
import csv
f = open("world_alcohol.csv")
reader = csv.reader(f)
world_alchol = list(reader)
print(world_alchol[0])
year = []
for row in world_alchol:
    year.append(row[3])
year = year[1:]

total = 0
for row in year:
    total += float(row)

print(total/len(year))

#Using NumPy
import numpy
world_alcohol = numpy.genfromtxt("world_alcohol.csv",delimiter = ",")
print(world_alcohol[0:3])

#Array shape
#It's useful to know how many elements an array contains.
#shape property on arrays to figure out haw many elements are in an array.
vector = numpy.array([10,20,30])
matrix = numpy.array([[5,10,15],[20,25,30],[35,40,45]])
vector_shape = vector.shape
matrix_shape = matrix.shape
print(vector_shape)
print(matrix_shape)

#Data type
#Each value in NumPy array has to have same data type.
#NumPy will automatically figure out an appropriate data type when reading in data or converting lists to array.
world_alcohol_dtype = world_alcohol.dtype
print(world_alcohol_dtype)

#Insepecting the data
#the genfromtxt() method will attept to guess the correct data type of the array it creates

#Reading in the data properly
#We can fix this mistake by specifying in the genfromtxt() method that we want to read in all the data strings.
world_alcohol = numpy.genfromtxt("world_alcohol.csv",delimiter=",",dtype="U75",skip_header=True)
#U75 that specifies we want to read in each value as a 75 byte unicode data type.
print(world_alcohol[0:5])
print(world_alcohol[3,3]) #extract the value in 3rd row 3rd column
print(world_alcohol[0:3,0:3]) #extract the array from 0 ro 3rd row, from 0 to 3rd column
