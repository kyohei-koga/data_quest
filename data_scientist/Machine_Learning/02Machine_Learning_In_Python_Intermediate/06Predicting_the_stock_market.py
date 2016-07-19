
# coding: utf-8

# You'll be using this dataset to develop a predictive model. You'll train the model with data from 1950-2012, and try to make predictions from 2013-2015.

# In[24]:

import pandas as pd
from datetime import datetime

sphist = pd.read_csv('sphist.csv')
#Convert the Date column to a Pandas date type.
sphist['Date'] = pd.to_datetime(sphist['Date'])
#print sphist['Date'] > datetime(year=2015,month=4,day=1)
sphist = sphist.sort_values('Date',ascending=True)


# Stock market data is sequential, and each observation comes a day after the previous observation. Thus, the observations are not all independent, and you can't treat them as such.This means you have to be extra careful to not inject "future" knowledge into past rows when you do training and prediction. 
# 
# Injecting future knowledge will make our model look good when you're training and testing it, but will make it fail in the real world. This is how many algorithmic traders lose money.
# 
# The time series nature of the data means that can generate indicators to make our model more accurate. 
# 
# When you do this, you have to be careful not to use the current row in the values you average.
# 
# Here are some indicators that are interesting to generate for each row:
# - The average price from the past 5 days.
# - The average price for the past 30 days.
# - The average price for the past 365 days.
# - The ratio between the average price for the past 5 days, and the average price for the past 365 days.
# - The standard deviation of the price over the past 5 days.
# - The standard deviation of the price over the past 365 days.
# - The ratio between the standard deviation for the past 5 days, and the standard deviation for the past 365 days.

# In[25]:

sphist.columns


# In[26]:

sphist['day_5_av'] = pd.rolling_mean(sphist.shift()['Close'],window=5)
sphist['day_5_std'] = pd.rolling_std(sphist.shift()['Close'],window=5)
sphist['avratio_5_365'] = sphist['day_5_av'] / pd.rolling_mean(sphist.shift()['Close'],window=365)


# In[28]:

sphist = sphist[sphist['Date']>datetime(year=1951,month=1,day=3)]
sphist = sphist.dropna(axis=0)


# In[30]:

train = sphist[sphist['Date'] < datetime(year=2013,month=1,day=1)]
test = sphist[sphist['Date'] >= datetime(year=2013,month=1,day=1)]


# # Making predictions
# It's recommended to use Mean Absolute Error, also called MAE, as an error metric, because it will show you how "close" you were to the price in intuitive terms. Mean Squared Error, or MSE, is an alternative that is more commonly used, but makes it harder to intuitively tell how far off you are from the true price because it squares the error.

# In[58]:

from sklearn.linear_model import LinearRegression
import numpy as np

model = LinearRegression()
model.fit(train[['day_5_av',]],train['Close'])
predict = model.predict(test[['day_5_av']])
abs_error = np.mean(abs(test['Close']-predict))
ms_error = np.mean((test['Close']-predict)**2)


# In[59]:

print abs_error,ms_error


# # Improving error
# You can improve the error of this model significantly, though. Think about some indicators that might be helpful to compute.Here are some ideas that might be helpful:
# - The average volume over the past five days.
# - The average volume over the past year.
# - The ratio between the average volume for the past five days, and the average volume for the past year.
# - The standard deviation of the average volume over the past five days.
# - The standard deviation of the average volume over the past year.
# - The ratio between the standard deviation of the average volume for the past five days, and the standard deviation of the average volume for the past year.
# - The year component of the date.
# - The ratio between the lowest price in the past year and the current price.
# - The ratio between the highest price in the past year and the current price.
# - The year component of the date.
# - The month component of the date.
# - The day of week
# - The day component of the date.
# - The number of holidays in the prior month.
# Add 2 additional indicators to your dataframe, and see if the error is reduced. You'll need to insert these indicators at the same point where you insert the others, before you clean out rows with NaN values and split the dataframe into train and `test.

# In[56]:

model = LinearRegression()
model.fit(train[['day_5_av','day_5_std']],train['Close'])
predict = model.predict(test[['day_5_av','day_5_std']])
abs_error = np.mean(abs(test['Close']-predict))
ms_error = np.mean((test['Close']-predict)**2)


# In[57]:

print abs_error,ms_error

