#coding: UTF-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#So far, you've learned how to plot data using 3 different techniques:

#    Matplotlib's high-level plotting methods - e.g. .scatter(), .plot()
#    Seaborn's high-level plotting methods - e.g. .distplot(), .boxplot()
#    Pandas DataFrame methods - e.g. .hist(), .boxplot()
# We'll be focusing now on the different components of Matplotlib so you can create more customizable data visualizations.

#Levels of abstraction
#There are many ways to create the same plot in Matplotlib and most of the differences come down to
#the level of abstraction you want to work with for a specific task!

month = [1,1,2,2,4,5,5,7,8,10,10,11,12,12]
temperature = [32,15,40,35,50,55,52,80,85,60,57,45,35,105]
plt.xlabel("month")
plt.ylabel("temperature")
plt.scatter(month,temperature)
plt.show()

#High level of abstraction
#in the previous code, you only had to provide the data and select the plot you want, this is the highest level of abstraction.
#While this level of abstraction is convenient for visualizing data quickly using standard plots,
#it doesn't provide us the flexibility to create more custom plots.

#Figures and Subplots
#Figure is the top-level Matplotlib object that manages the entire plotting area.
#A Figure instance acts as a container for your plots and contains some useful parameters and methods like:
#    The figsize(w,h) parameter lets you specify the width w and height h, in inches, of the plotting area
#    The dpi parameter lets you specify the density, in dots per inch
#    The .add_subplot() method lets you add individual plots to the Figure instance

#Subplot is the Matplotlib object that you use to create the axes for a plot.
#While a Figure can contain multiple subplots that are laid out on a grid, we'll start with just one plot.
#In the following code cell, we:
#    call plt.figure() to instantiate a new Figure instance (width: 5 inches, height: 7 inches)
#    assign the Figure to the variable fig
#    call .add_subplot(1,1,1) on the Figure instance to add an empty plot
#    assign the Subplot to the variable ax
#    call plt.show() to display our wonderful creation

#You'll notice we passed 1,1,1 into the Figure's .add_subplot() method.
#This style is called grid notation and you use it to express the layout of plots and which plot
#you want returned from that function call. You can break grid notation down into the 3 parameters:
#    the first parameter refers to the row number 1
#    the second parameter refers to the column number 2
#    the third parameter refers to the nth plot in the Figure to be returned (only 1 plot in this case)

fig = plt.figure(figsize=(5,7))
ax = fig.add_subplot(1,1,1)
plt.show()

#Axes
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim([0,14]) #sset_xlim() attribute change xrange.
plt.show()

#Practice

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim([np.min(month),np.max(month)]) #sset_xlim() attribute change xrange.
ax.set_ylim([np.min(temperature),np.max(temperature)])
#plt.show()

#Adding data
#makea a scatter graph , adjast color and marker type.
color = "darkblue"
marker = "o"

ax.scatter(month,temperature,color=color,marker=marker)
plt.show()

#Customizing the plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim(0,13) #X range
ax.set_ylim(10,110) #Y range
ax.set_xlabel("Month")
ax.set_ylabel("Temperature")
ax.set_title("Year round Temperature")
ax.scatter(month,temperature,color=color,marker="*")
plt.show()

#Setting multiple attributes easily
#.set() method is to specify all the attribute easily
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set(xlim=(0,13),ylim=(10,110),xlabel="Month",ylabel="Temperature",title="Year round Temperature")
ax.scatter(month,temperature,color=color,marker="*")
plt.show()

#Multiple subplots
#If you wanted our Figure instance to have 2 plots on the same grid, you'll need to modify the parameters you pass to .add_subplot().
#Recall the parameters for the .add_subplot() function
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
plt.show()

#Adding data to multiple subplots
month_2013 = [1,2,3,4,5,6,7,8,9,10,11,12]
temperature_2013 = [32,18,40,40,50,45,52,70,85,60,57,45]
month_2014 = [1,2,3,4,5,6,7,8,9,10,11,12]
temperature_2014 = [35,28,35,30,40,55,50,71,75,70,67,49]
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.set(xlim=[0,13],ylim=[10,110],xlabel="month_2013",ylabel="temprature_2013",title="2013")
ax1.scatter(month_2013,temperature_2013,color="darkblue",marker="o")
ax2.set(xlim=[0,13],ylim=[10,110],xlabel="month_2014",ylabel="temprature_2014",title="2014")
ax2.scatter(month_2014,temperature_2014,color="darkgreen",marker="o")
plt.show()
