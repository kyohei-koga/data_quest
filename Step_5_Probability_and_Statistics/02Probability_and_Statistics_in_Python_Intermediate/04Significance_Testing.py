
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')


# # Hypothesis testing
# We use hypothesis testing to determine if a change we made had a meaningful impact or not. 
# 
# We first set up a null hypothesis that describes the status quo. We then state an alternative hypothesis, which we used to compare with the null hypothesis to decide which describes the data better. In the end, we either need to:
# - reject the null hypothesis and accept the alternative hypothesis or
# - accept the null hypothesis and reject the alternative hypothesis.

# # Research design
# To help us determine if the weight loss pill was effective, we conducted a study where we invited 100 volunteers and split them into 2 even groups randomly:
# - Group A was given a placebo, or fake, pill and instructed to consumer it on a daily basis.
# - Group B was given the actual weight loss pill and instructed to consume it on a daily basis.
# This type of study is called a blind experiment since the participants didn't know which pill they were receiving. This helps us reduce the potential bias that is introduced when participants know which pill they were given. For example, participants who are aware they were given the weight loss pill may try to add healthier foods to their diet to help them lose more weight. 
# 
# Understanding the research design for a study is an important first step that informs the rest of your analysis. It helps us uncover potential flaws in the study that we need to keep in mind as we dive deeper. The weight loss pill study we conducted is known as an experimental study. Experimental studies usually involve bringing in participants, instructing them to perform some tasks, and observing them. A key part of running an experimental study is random assignment, which involves assigning participants in the study to random groups without revealing which group each participant is in. Before exploring and analyzing a dataset, it's important to understand how the study was conducted. Flaws in how the study was run can lead you to reach the wrong conclusions.

# # Statistical significance
# Statistics helps us determine if the difference in the weight lost between the 2 groups is because of random chance or because of an actual difference in the outcomes.
# 
#  Our null hypothesis should describe the default position of skepticism, which is that there's no statistically significant difference between the outcomes of the 2 groups. Put another way, it should state that any difference is due to random chance. Our alternative hypothesis should state that there is in fact a statistically significant difference between the outcomes of the 2 groups.
#  - Null hypothesis: participants who consumed the weight loss pills lost the same amount of weight as those who didn't take the pill.
#  - Alternative hypothesis: participants who consumed the weight loss pills lost more weight than those who didn't take the pill.
#  

# In[6]:

import numpy as np
import matplotlib.pyplot as plt
weight_lost_a = [3, 2, 3, 4, 3, 2, 2, 2, 1, 3, 2, 3, 1, 3, 4, 1, 3, 2, 1, 3, 4, 3, 2, 3, 7, 2, 3, 2, 5, 1, 1, 1, 3, 2, 4, 10, 2, 3, 2, 5, 6, 2, 3, 2, 3, 4, 1, 3, 3, 1]
weight_lost_b = [5, 4, 5, 5, 4, 5, 7, 5, 4, 3, 3, 5, 10, 3, 4, 9, 7, 6, 9, 4, 2, 5, 7, 7, 7, 5, 4, 8, 9, 6, 7, 6, 7, 6, 3, 5, 5, 4, 2, 3, 3, 5, 6, 9, 7, 6, 4, 5, 4, 3]

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)
plt.hist(weight_lost_a)
plt.show()
plt.hist(weight_lost_b)
plt.show()


# # Test statistic
# To decide which hypothesis more accurately describes the data, we need to frame the hypotheses more quantitatively. The first step is to decide on a test statistic, which is a numerical value that summarizes the data and we can use in statistical formulas. We use this test statistic to run a statistical test that will determine how likely the difference between the groups were due to random chance. 
# 
# Since we want to know if the amount of weight lost between the groups is meaningfully different, we will use the difference in the means, also known as the mean difference, of the amount of weight lost for each group as the test statistic. 
# 
# Null hypothesis: x¯b−x¯a=0
# 
# Alternative hypothesis: x¯b−x¯a>0

# In[7]:

mean_difference = mean_group_b - mean_group_a
print mean_difference


# # Permutation test
# Now that we have a test statistic, we need to decide on a statistical test. The purpose of a statistical test is to work out the likelihood that the result we achieved was due to random chance.
# 
# The permutation test is a statistical test that involves simulating rerunning the study many times and recalculating the test statistic for each iteration. The goal is to calculate a distribution of the test statistics over these many iterations. This distribution is called the sampling distribution and it approximates the full range of possible test statistics under the null hypothesis. We can then benchmark the test statistic we observed in the data (a mean difference of 2.52) to determine how likely it is to observe this mean difference under the null hypothesis. If the null hypothesis is true, that the weight loss pill doesn't help people lose more weight, than the observed mean difference of 2.52 should be quite common in the sampling distribution. If it's instead extremely rare, then we accept the alternative hypothesis instead.
# 
# To simulate rerunning the study, we randomly reassign each data point (weight lost) to either group A or group B. We keep track of the recalculated test statistics as a separate list. By re-randomizing the groups that the weight loss values belong to, we're simulating what randomly generated groupings of these weight loss values would look like. We then use these randomly generated groupings to understand how rare the groupings in our actual data were.

# In[12]:

all_values = [3, 5, 2, 4, 3, 5, 4, 5, 3, 4, 2, 5, 2, 7, 2, 5, 1, 4, 3, 3, 2, 3, 3, 5, 1, 10, 3, 3, 4, 4, 1, 9, 3, 7, 2, 6, 1, 9, 3, 4, 4, 2, 3, 5, 2, 7, 3, 7, 7, 7, 2, 5, 3, 4, 2, 8, 5, 9, 1, 6, 1, 7, 1, 6, 3, 7, 2, 6, 4, 3, 10, 5, 2, 5, 3, 4, 2, 2, 5, 3, 6, 3, 2, 5, 3, 6, 2, 9, 3, 7, 4, 6, 1, 4, 3, 5, 3, 4, 1, 3]
mean_differences = []

for i in range(1000):
    group_a = []
    group_b = []
    for value in all_values:
        random_value = np.random.rand()
        if random_value >= 0.5:
            group_a.append(value)
        else:
            group_b.append(value)
    mean_a = np.mean(group_a)
    mean_b = np.mean(group_b)
    iteration_mean_difference = mean_b - mean_a
    mean_differences.append(iteration_mean_difference)

plt.hist(mean_differences)
plt.show()


# # Dictionary representation of a distribution
# To check if a key exists in a dictionary, we need to use the get() method to:
# - return the value at the specified key if it exists in the dictionary or
# - return another value we specify instead.
# 
# Here are the parameters the method takes in:
# 
# - the required parameter is the key we want to look up,
# - the optional parameter is the default value we want returned if the key is not found.
# 

# In[13]:

sampling_distribution = {}
for difference in mean_differences:
    if sampling_distribution.get(difference,False):
        sampling_distribution[difference] += 1
    else:
        sampling_distribution[difference] = 1


# # P value
# In the sampling distribution we generated, most of the values are closely centered around the mean difference of 0. This means that if it were purely up to chance, both groups would have lost the same amount of weight (the null hypothesis). But since the observed test statistic is not near 0, it could mean that the weight loss pills could be responsible for the mean difference in the study.
# 
# We can now use the sampling distribution to determine the number of times a value of 2.52 or higher appeared in our simulations. If we then divide that frequency by 1000, we'll have the probability of observing a mean difference of 2.52 or higher purely due to random chance.
# 
# This probability is called the p value. If this value is high, it means that the difference in the amount of weight both groups lost could have easily happened randomly and the weight loss pills probably didn't play a role. On the other hand, a low p value implies that there's an incredibly small probability that the mean difference we observed was because of random chance.
# 
# The most common p value threshold is 0.05 or 5%, which is what we'll use in this mission. Although .05 is an arbitrary threshold, it means that there's only a 5% chance that the results are due to random chance, which most researchers are comfortable with.

# # Caveats
# Since the p value of 0 is less than the threshold we set of 0.05, we conclude that the difference in weight lost can't be attributed to random chance alone. We therefore reject the null hypothesis and accept the alternative hypothesis. A few caveats:
# - Research design is incredibly important and can bias your results. For example, if the participants in group A realized they were given placebo sugar pills, they may modify their behavior and affect the outcome.
# - The p value threshold you set can also affect the conclusion you reach.
#  - If you set too high of a p value threshold, you may accept the alternative hypothesis incorrectly and fail to reject the null hypothesis. This is known as a type I error.
#  - If you set too low of a p value threshold, you may reject the alternative hypothesis incorrectly in favor of accepting the null hypothesis. This is known as a type II error.

# In[ ]:



