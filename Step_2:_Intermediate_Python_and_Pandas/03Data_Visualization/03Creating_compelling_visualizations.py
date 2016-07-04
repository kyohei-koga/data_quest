#coding: UTF-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

recent_grads=pd.read_csv("recent-grads.csv")
print(recent_grads.head(3))

#Histogram: distplot()
#Pandas .hist() function, which uses Matplotlib under the hood.
#Unfortunately, the resulting plot wasn't very visually compelling since it used Matplotlib's default styling.

sns.distplot(recent_grads['Full_time_year_round'],kde=False)
#kde:Kernel density estimation
sns.plt.show()

#comparing
#You'll notice that the plot will be formatted using Seaborn's style instead of the default Matplotlib styles
#that Pandas uses since Seaborn was imported to the environment and overrode the default styles.
recent_grads.hist(['Full_time_year_round'])
sns.plt.show()

#Customizing histogram: distplot()
#As we mentioned before, there are 2 primary ways to customize how a Seaborn plot looks:
#    Plotting function parameters, e.g. sns.distplot(kde=False)
#    Seaborn functions, called on the sns Seaborn object synonym

sns.distplot(recent_grads["Median"],kde=False)
sns.axlabel('Median','Frequency') #name x,y labels
sns.plt.show()
recent_grads.hist(["Median"])
plt.xlabel("Median")
plt.ylabel("Frequency")
plt.show()

#Boxplots: boxplot()
#The documentation for the .boxplot() function can be found below URL
#https://stanford.edu/~mwaskom/software/seaborn/generated/seaborn.boxplot.html
sns.boxplot(x=recent_grads["Major_category"],y=recent_grads["Median"])
sns.plt.show()

#Pair plot: pairplot()
# we can use a Seaborn pair plot to automatically visualize all combinations of variables from columns in a DataFrame.
#To demonstrate how straightforward the syntax is for generating a pair plot, and most other plots as well, in Seaborn,
# we're going to ask you to generate a pair plot by reading the documentation on the .pairplot() method.

sns.pairplot(recent_grads,vars=["Median","College_jobs","Total"])
sns.plt.show()
