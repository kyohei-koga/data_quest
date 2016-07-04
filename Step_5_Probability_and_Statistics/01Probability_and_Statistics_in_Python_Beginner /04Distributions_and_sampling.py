#coding: UTF-8

import pandas as pd
import re

data = pd.read_csv("ACS_13_5YR_DP03_with_ann.csv",header=1)
column = data.columns
column = ["Id2","Geography","Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - Total households - Median household income (dollars)",
"Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - Total households - Mean household income (dollars)",
"Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - Families - Median family income (dollars)",
"Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - Per capita income (dollars)",
"Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - Nonfamily households - Median nonfamily income (dollars)",
"Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - With Social Security - Mean Social Security income (dollars)",
"Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - Families - Mean family income (dollars)"]

income = data[column]
names = {"Geography":"county",
"Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - Total households - Median household income (dollars)":"pop_over_25",
"Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - Total households - Mean household income (dollars)":"median_income",
"Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - Families - Median family income (dollars)":"median_income_no_hs",
"Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - Per capita income (dollars)":"median_income_hs",
"Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - Nonfamily households - Median nonfamily income (dollars)":"median_income_some_college",
"Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - With Social Security - Mean Social Security income (dollars)":"median_income_college",
"Estimate; INCOME AND BENEFITS (IN 2013 INFLATION-ADJUSTED DOLLARS) - Families - Mean family income (dollars)":"median_income_graduate_degree"}
income.rename(columns=names,inplace=True)

#Exploring the data
lowest_income_county = income["county"][income["median_income"].idxmin()]
high_pop = income[income["pop_over_25"] > 100000]
lowest_income_high_pop_county = high_pop["county"][high_pop["median_income"].idxmin()]

#Random numbers
#Sometimes, instead of looking at a whole dataset, you just want to take a sample of it. This usually happens when dealing with the whole set of data is impractical.
#We'll get into how a sample and a full population compare shortly. For now, let's look at how we can generate a random sample.

import random
# Returns a random integer between the numbers 0 and 10, inclusive.
num = random.randint(0,10)

# Generate a sequence of 10 random numbers between the values of 0 and 10.
random_sequence = [random.randint(0,10) for _ in range(10)]
# Sometimes, when we generate a random sequence, we want it to be the same sequence whenever the program is run.
# An example is when you use random numbers to select a subset of the data, and you want other people
# looking at the same data to get the same subset.
# We can ensure this by setting a random seed.
# A random seed is an integer that is used to "seed" a random number generator.
# After a random seed is set, the numbers generated after will follow the same sequence.
random.seed(10)
print([random.randint(0,10) for _ in range(5)])
#Same swquence as above
random.seed(10)
print([random.randint(0,10) for _ in range(5)])

#Selecting items from a list
#When we do sampling, we usually want to select a certain number of items from a list. There are a few ways to do this.
#The easiest way is to use the random.sample method to select a specified number of items from a list.

shopping = [300, 200, 100, 600, 20]
random.seed(1)
shopping_sample = random.sample(shopping,4)
print(shopping_sample)

#Population vs sample
# This means that the probabilities we observe are not necessarily the true probabilities of an event occuring.
#As you may be able to guess, the larger the sample size (in this case, the more rolls we perform), the closer to the "true" probabilities we get. Let's explore this more.
import matplotlib.pyplot as plt

def roll():
    return random.randint(1,6)

random.seed(1)
small_sample = [roll() for _ in range(10)]
plt.hist(small_sample,bins=6)
plt.show()

random.seed(1)
medium_sample = [roll() for _ in range(100)]
plt.hist(medium_sample,bins=6)
plt.show()

random.seed(1)
large_sample = [roll() for _ in range(10000)]
plt.hist(large_sample,bins=6)
plt.show()

#Finding the right sample size
#We can graph out this variability by repeatedly rolling the die N times. So we could do 20 trials of rolling the die 10 times, and graph out all the resulting probabilities of rolling a 1. This would tell us how much error we could expect by rolling the die 20 times.

def probability_of_one(num_trials,num_rolls):
    #This function will take in the number of trials, and the number of rolls per trial.
    #Then it will conduct each trial, and record the probability of rolling a one.
    probabilities = []
    for i in range(num_trials):
        die_rolls = [roll() for _ in range(num_rolls)]
        one_prob = len([d for d in die_rolls if d == 1]) / float(num_rolls)
        probabilities.append(one_prob)
    return probabilities

random.seed(1)
small_sample = probability_of_one(300,50)
plt.hist(small_sample,bins=20)
plt.show()

random.seed(1)
medium_sample = probability_of_one(300,100)
plt.hist(medium_sample,bins=20)
plt.show()

random.seed(1)
large_sample = probability_of_one(300,1000)
plt.hist(large_sample,bins=20)
plt.show()

#What are the odds
#if we do 100 rolls of the die, and get a .25 probability of rolling a 1, we could look up how many trials in our data above got that probability or higher for one.
import numpy as np
large_sample_std = np.std(large_sample)
avg = np.mean(large_sample)
deviations_from_mean = (.18 - avg) / large_sample_std

over_18_count = len([p for p in large_sample if p >= .18])

#Sampling counties
#Now, let's look at why random sampling is important instead of just picking any rows we want.
mean_median_income = income["median_income"].mean()
print(mean_median_income)
def get_sample_mean(start,end):
    return income["median_income"][start:end].mean()

def find_mean_incomes(row_step):
    mean_median_sample_incomes = []
    # Iterate over the indices of the income rows
    # Starting at 0, and counting in blocks of row_step (0, row_step, row_step * 2, etc).
    for i in range(0,income.shape[0], row_step):
        # Find the mean median for the row_step counties from i to i+row_step.
        mean_median_sample_incomes.append(get_sample_mean(i, i+row_step))
    return mean_median_sample_incomes

nonrandom_sample = find_mean_incomes(100)
plt.hist(nonrandom_sample,20)
plt.show()

# What you're seeing above is the result of biased sampling.
# Instead of selecting randomly, we selected counties that were next to each other in the data.
# This picked counties in the same state more often that not, and created means that didn't represent the whole country.
# This is the danger of not using random sampling -- you end up with samples that don't reflect the entire population.
# This gives you a distribution that isn't normal.

def select_random_sample(count):
    random_indices = random.sample(range(0, income.shape[0]),count)
    return income.iloc[random_indices]

random.seed(1)
random_sample = [select_random_sample(100)["median_income"].mean() for _ in range(1000)]
plt.hist(random_sample, 20)
plt.show()

#An experiment
#We want to run an experiment to see whether a certain kind of adult education can help high school graduates earn more relative to college graduates than they could otherwise.
random.seed(1)
mean_ratios = []
for i in range(1000):
    sample = select_random_sample(100)
    ratios = sample["median_income_hs"] / sample["median_income_college"]
    mean_ratios.append(ratios.mean())

plt.hist(mean_ratios, bins=20)
plt.show()

#Statistical significance
#Now that we have our result, how do we know if our hypothesis is correct? Remember, our hypothesis was about the whole population, not about the sample.
#Statistical significance is used to determine if a result is valid for a population or not.
#A common significance level is .05. This means: "only 5% or less of the time will the result have been due to chance".
#In our case, chance could be that the high school graduates in the county changed income some way other than through our program -- maybe some higher paying factory jobs came to town, or there were some other educational initiatives around.
significance_value = None
mean_higher = len([m for m in mean_ratios if m >= .675])
significance_value = mean_higher / len(mean_ratios)

#Our significance value was .014. Based on the entire population, only 1.4% of the time will the wage results we saw have occurred on their own. So our experiment exceeded our significance level (lower means more significant). Thus, our experiment showed that the program did improve the wages of high school graduates relative to college graduates.
