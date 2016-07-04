
# coding: utf-8

# In[12]:

get_ipython().magic(u'matplotlib inline')
import pandas as pd
column_names = ["name","landmass","zone","area","population","language","relegion","bars","stripes","colpurs","red",
               "green","blue","gold","white","black","orange","mainhue","circles","crosses","saltires","quarters",
               "sunstars","crescent","triangle","icon","animate","text","topleft","botright"]

flags = pd.read_csv("flag.data",header=None,names=column_names)


# # Calculating probability
# Probability can roughly be described as "the percentage chance of an event or sequence of events occuring".
# We could compute the probability of a country flag having a certain characteristic by dividing how many flags have that characteristic by the total number of flags.

# In[13]:

total_countries = flags.shape[0]
orange_probability = flags[flags["orange"]==1].shape[0] / float(total_countries)
orange_probability


# # Conjunctive probabilities
# But let's say we have a coin that we flip 5 times, and we want to find the probability that it will come up heads every time. This is called a conjunctive probability, because it involves a sequence of events. 

# # Dependent probabilities
# Let's say that we're picking countries from the sample, and removing them when we pick. Each time we pick a country, we reduce the sample size for the next pick. The events are dependent -- the number of countries available to pick depends on the previous pick. We can't just calculate the probability upfront and take a power in this case 
# Let's simplify the example a bit by saying that we're eating some M&Ms. There are 10 M&Ms left in the bag: 5 are green, and 5 are blue. What are the odds of getting 3 blue candies in a row? The probability of getting the first blue candy is 5/10, or 1/2. When we pick a blue candy, though, we remove it from the bag, so the probability of getting another is 4/9. The probability of picking a third blue candy is 3/8. This means our final probability is 1/2 * 4/9 * 3/8, or .0833. So, there is an 8.3% chance of picking three blue candies in a row.

# In[14]:

total_count = flags.shape[0]
red_count = flags[flags["red"] == 1].shape[0]
one_red = red_count / float(total_count)
two_red = one_red * ((red_count -1 ) / float(total_count - 1))
three_red = two_red * ((red_count -2) / float(total_count - 2))
print one_red,two_red,three_red


# # Disjunctive probability
# What if we want to know the probability of rolling a 2 or the probability of rolling a three? We actually can just add the probabilities, because both events are independent. Rolling a 2 doesn't change my odds of rolling a three next time around. Thus, the probability is 1/6 + 1/6, or 1/3.

# # Disjunctive dependent probabilities
# But, let's think about a slightly more complex case with dependencies. What if we have a set of 10 cars -- 5 are red and 5 are blue. 5 of the 10 are convertibles, and 5 are sport utility vehicles. 
# If we wanted to find cars that were red or were convertibles, we might try to add the probability of the car being red to the probability of the car being a convertible. This would give us 1/2 + 1/2 == 1. But, this is wrong, as it tells us that all 10 cars are either red or convertibles.
# It's wrong because it assumes that the two traits (color and vehicle type) are independent, when in fact they aren't. Some of the cars are red and convertibles. If we don't account for this overlap, we end up with a vastly inflated count.

# In[15]:

stripes_or_bars = None
red_or_orange = None
red = flags[flags["red"] == 1].shape[0] / float(flags.shape[0])
orange = flags[flags["orange"] == 1].shape[0] / float(flags.shape[0])
red_and_orange = flags[(flags["red"] == 1) & (flags["orange"] == 1)].shape[0] / float(flags.shape[0])

red_or_orange = red + orange - red_and_orange
print red_or_orange

