#coding: UTF-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Data visualization is the dominant technique within data exploration that allows you to develop
#some initial hypothese for the relationships between variables and some general trends that
#will help you navigate your data workflow better.

recent_grads = pd.read_csv("recent-grads.csv")
print(recent_grads.columns)

#Histograms
#A histogram is a graph that enables you to visualize the distribution of values of a column.
#pandas.dataframe.hist document is below
#Draw histogram of the DataFrame’s series using matplotlib / pylab.
#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html#pandas-dataframe-hist

columns = ['Median','Sample_size']
#Set the layout parameters as (2,1) so the graphs are displayed as 2 rows & 1column
recent_grads.hist(column=columns,layout=(2,1),grid=False,bins=50)
plt.show()
#Practice: histograms
#By default, the .hist() method uses 10 as the number of bins, but you can specify a different value using the bins parameter.

#Box plots
sample_size = recent_grads[["Sample_size","Major_category"]]
#Run the boxplot() function on sample_size DataFrame and specify, as a parameter
#that we'd like a box and whisker to be generated for each unique Major_category
sample_size.boxplot(by="Major_category")
# Format the resulting plot to make the x-axis labels (each `Major_category` value)
# appear vertically instead of horizontally (by rotating 90 degrees)
plt.xticks(rotation=90)
plt.show()

recent_grads[["Sample_size","Major_category"]].boxplot(by="Major_category")
plt.xticks(rotation=90)
recent_grads[["Total","Major_category"]].boxplot(by="Major_category")
plt.xticks(rotation=90)
plt.show()

#8: Multiple plots in one chart
#We then use the color parameter to plot each scatter plot using a different color so we can easily see the difference.
plt.scatter(recent_grads['Unemployment_rate'],recent_grads['Median'],color='red')
plt.scatter(recent_grads['ShareWomen'],recent_grads['Median'],color='blue')
plt.show()
