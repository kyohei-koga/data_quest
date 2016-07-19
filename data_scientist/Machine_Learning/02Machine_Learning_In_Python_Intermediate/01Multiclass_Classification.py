
# coding: utf-8

# # Introduction To The Data
# For each car we have information about the technical aspects of the vehicle such as the motor's displacement, the weight of the car, the miles per gallon, and how fast the car accelerates. 
# 
# Using this information we will predict the origin of the vehicle, either North America, Europe, or Asia.

# In[18]:

import pandas as pd
import numpy as np

columns_name = ["mpg","cylinders","displacement","horsepower","weight","acceleration","year","origin","car_name"]
cars = pd.read_csv('auto-mpg.data',delim_whitespace=True,names=columns_name)
unique_regions = cars['origin'].unique()
print(unique_regions)


# # Dummy Variables
# In many cases you'll have to create numeric representation of categorical values yourself.
# 
# We must use dummy variables for columns containing categorical values.Whenever we have more than 2 categories, we need to create more columns to represent the categories. Since we have 5 different categories of cylinders, we could use 3, 4, 5, 6, and 8 to represent the different categories. We can split the column into separate binary columns.
# 
# We can use the Pandas function get_dummies to return a Dataframe containing binary columns from the values in the cylinders column.
# 
# We then use the Pandas function concat to add the columns from this Dataframe back to cars.

# In[19]:

dummy_cylinders = pd.get_dummies(cars['cylinders'],prefix='cyl')
cars = pd.concat([cars,dummy_cylinders],axis=1)

dummy_years = pd.get_dummies(cars['year'],prefix='year')
cars = pd.concat([cars,dummy_years],axis=1)
cars.drop('year',axis=1)
cars.drop('cylinders',axis=1)
print(cars.head())


# # Multiclass Classification
# When we have 3 or more categories, we call the problem a multiclass classification problem.There are a few different methods of doing multiclass classification and in this mission, we'll focus on the one-versus-all method.
# 
# The one-versus-all method is a technique where we choose a single category as the Positive case and group the rest of the categories as the False case. We're essentially splitting the problem into multiple binary classification problems. For each observation, the model will then output the probability of belonging to each category.

# In[22]:

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]
train = shuffled_cars[0:int(cars.shape[0]*0.7)]
test = shuffled_cars[int(cars.shape[0]*0.7):]


# # Training A Multiclass Logistic Regression Model
# In the one-vs-all approach, we're essentially converting an n-class (in our case n is 3) classification problem into n binary classification problems. For our case, we'll need to train 3 models:
# - A model where all cars built in North America are considered Positive (1) and those built in Europe and Asia are considered Negative (0).
# - A model where all cars built in Europe are considered Positive (1) and those built in North America and Asia are considered Negative (0).
# - A model where all cars built in Asia are labeled Positive (1) and those built in North America and Europe are considered Negative (0).
# 
# For each observation, we choose the label corresponding to the model that predicted the highest probability.
# 
# We'll use the binary features we created from the cylinders and year columns to train 3 models using the LogisticRegression class from scikit-learn.

# In[28]:

from sklearn.linear_model import LogisticRegression

unique_origins = cars['origin'].unique() #countries where made in
unique_origins.sort()

models = {}
features = [c for c in train.columns if c.startswith('cyl') or c.startswith('year')]

for origin in unique_origins:
    model = LogisticRegression()
    
    X_train = train[features]
    y_train = train['origin'] == origin
    
    model.fit(X_train,y_train)
    models[origin] = model


# # Testing The Models

# In[37]:

testing_probs = pd.DataFrame(columns=unique_origins)
for origin in unique_origins:
    X_test = test[features]
    testing_probs[origin] = models[origin].predict_proba(X_test)[:,1] #1 indicates positive probability


# # Choose The Origin
# To classify each observation we want to select the origin with the highest probability of classification for that observation.
# 
# While each column in our dataframe testing_probs represents an origin we just need to choose the one with the largest probability. We can use the Dataframe method .idxmax() to return a Series where each value corresponds to the column or where the maximum value occurs for that observation. We need to make sure to set the axis paramater to 1 since we want to calculate the maximum value across columns.

# In[40]:

predicted_origins = testing_probs.idxmax(axis=1)
print(predicted_origins)


# In[ ]:



