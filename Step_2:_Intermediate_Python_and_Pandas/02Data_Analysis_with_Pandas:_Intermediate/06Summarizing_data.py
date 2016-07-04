#coding: UTF-8
#practice mission
import pandas as pd
import numpy as np

#read csv data
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
print(all_ages.columns)
print(recent_grads.columns)

#we would like to know the total number of people in each Major_category for both datasets.
#All values for Major_category
print(all_ages["Major_category"].value_counts().index) #.value_counts method returns count of each row values
all_ages_major_categories = dict()
recent_grads_major_categories = dict()

for row in all_ages["Major_category"].value_counts().index:
    condition = all_ages[all_ages["Major_category"] == row]
    all_ages_major_categories[row] = np.sum(condition["Total"])
#print(all_ages_major_categories)

for row in recent_grads["Major_category"].value_counts().index:
    condition = recent_grads[recent_grads["Major_category"] == row]
    recent_grads_major_categories[row] = np.sum(condition["Total"])

low_wadge_percent = np.sum(recent_grads["Low_wage_jobs"]) / np.sum(recent_grads["Total"].astype(float))
print(low_wadge_percent)

majors = recent_grads["Major"].value_counts().index
#print(recent_grads["Major_category"].value_counts())
recent_grads_lower_emp_count = 0
all_ages_lower_emp_count = 0

for major in majors:
    recent_grads_major = recent_grads[recent_grads["Major"] == major]
    all_ages_major = all_ages[all_ages["Major"] == major]

    recent_grads_umemp_rate = recent_grads_major["Unemployment_rate"].values[0] #values return as ndarray-like depending on the dtype, here, for converting series object to value
    all_ages_umemp_rate = all_ages_major["Unemployment_rate"].values[0]

    if recent_grads_umemp_rate < all_ages_umemp_rate:
        recent_grads_lower_emp_count += 1
    elif all_ages_umemp_rate < recent_grads_umemp_rate:
        all_ages_lower_emp_count += 1
