#coding: UTF-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

forest_fires = pd.read_csv("forestfires.csv")
print(forest_fires.columns)

#Scatter Plots
#A scater plot show the general correlation between two variables.

plt.scatter(forest_fires["wind"],forest_fires["area"])
plt.show()
plt.scatter(forest_fires["temp"],forest_fires["area"])
plt.show()

#Line Charts
#Line charts are used when the observations are related in some way
age = [5, 10, 15, 20, 25, 30]
height = [25, 45, 65, 75, 75, 75]
plt.plot(age,height)
plt.show()

#Bar graphs
#Bar graphs are used for communicating categorical information.
area_by_y = forest_fires.pivot_table(index="Y",values="area",aggfunc=np.mean)
plt.bar(area_by_y.index,area_by_y)
plt.show()

#Horizontal bar graphs
#A horizontal bar graph is much like a regular bar graph, but the bars are horizontal instead of vertical.
#This can be useful when communicating data that contains larger differences, as there tends to be more horizontal space on pages than vertical space.
area_by_month = forest_fires.pivot_table(index="month", values="area", aggfunc=np.mean)
plt.barh(area_by_month,range(len(area_by_month)))
plt.show()

#Chart labels
#You can add each element with a matplotlib method:
#    Title -- the title() method.
#    X axis label -- the xlabel() method.
#    Y axis label -- the ylabel() method.

plt.scatter(forest_fires["wind"],forest_fires["area"])
plt.title("Wind speed vs fire area")
plt.xlabel("Wind speed when fire startd")
plt.ylabel("Area consumed by fire")
plt.show()

#Plot Aesthetics
#Matplotlib has a few built-in styles that can be used, including:
#    fivethirtyeight -- the style of the plots on the site fivethirtyeight.com.
#    ggplot -- the style of the popular R plotting library ggplot.
#    dark_background -- will give the plot a darker background.
#    bmh -- the style used in a popular online statistics book.
plt.style.use("fivethirtyeight")
plt.plot(forest_fires["rain"],forest_fires["area"])
plt.show()
