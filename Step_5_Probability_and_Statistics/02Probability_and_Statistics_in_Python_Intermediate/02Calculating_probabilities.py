
# coding: utf-8

# In[3]:

get_ipython().magic(u'matplotlib inline')
import pandas as pd
bikes = pd.read_csv("bike_rental_day.csv")


# # Finding the number of combinations
# We can calculate probabilities greater than or equal to a threshold with our bike sharing data. We found that the probability of having more riders than 4000 is about .6. We can use this to find the probability that in 10 days, 7 or more days have more than 4000 riders

# In[5]:

import math
def find_outcome_combinations(N,k):
    numerator = math.factorial(N)
    denominator = math.factorial(k) * math.factorial(N - k)
    return numerator / float(denominator)
combination_7 = find_outcome_combinations(10,7)
combination_7


# # Statistical significance
# Typically, researchers will use 5% as a significance threshold -- if an event would only happen 5% or less of the time by random chance, then it is statistically significant. If an event would happen more than 5% of the time by random chance, then it isn't statistically significant.
# In our case, there is 12% chance that the weather would be sunny 8 days out of 10 by random chance. We add this to 4% for 9 days out of 10, and .6% for 10 days out of 10 to get a 16.6% total chance of the sunny outcome happening 8 or more time in our 10 days. Our result isn't statistically significant, so we'd have to go back to the lab and spend some time adding more flux capacitors to our weather control device.
