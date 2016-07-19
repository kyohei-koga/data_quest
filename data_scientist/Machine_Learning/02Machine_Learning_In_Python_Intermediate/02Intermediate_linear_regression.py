
# coding: utf-8

# In[2]:

import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

pisa = pd.DataFrame({'year':range(1975,1988),
                        'lean':[2.9642, 2.9644, 2.9656, 2.9667, 2.9673, 2.9688, 2.9696,
                               2.9698, 2.9713, 2.9717, 2.9725, 2.9742, 2.9757]})

plt.scatter(pisa['year'],pisa['lean'])
plt.show()


# # Fit the Linear Model
# Statsmodels is a library which allows for rigorous statistical analysis in python.For linear models, statsmodels provides ample statistical measures for proper evaluation.The class sm.OLS is used to fit linear models, standing for oridinary least squares.
# 
# OLS() does not automatically add an intercept to our model.We can add a column of 1's to add another coefficient to our model and since the coefficient is multiplied by 1 we are given an intercept.

# In[4]:

import statsmodels.api as sm

y = pisa.lean
X = pisa.year
X = sm.add_constant(X) #add a column of 1's as the constant term

#OLS -- Ordinary Least Square Fit
linear = sm.OLS(y,X)
linearfit = linear.fit()
print(linearfit.summary())


# # Define a Basic Linear Model
# We see that the printed summary contains a lot of information about our model.To understand these statistical measures we must start with a formal definition of a basic linear regression model. Mathematically, a basic linear regression model is defined as yi=β0+β1xi+ei where ei∼N(0,σ2) is the error term for each observation i where β0 is the intercept and β1 is the slope. 
# 
# - The residual for the prediction of observation i is ei=yi^−yi where yi^ is the prediction.
# 
# the model assumes that the errors, known as residuals, between our prediction and observed values are normally distributed and that the average error is 0. Estimated coefficients, those which are modeled, will be refered to as βi^ while βi is the true coefficient which we cannot calculated.
# 
# In the end, yi^=β0^+β1^xi is the model we will estimate.
# 

# In[5]:

yhat = linearfit.predict(X)
residuals = yhat - y


# # Histogram of Residuals
# We've used histograms in the past to visualize the distribution of our data.If the histogram of residuals look similar to a bell curve then we will accept the assumption of normality.
# 
# There are more rigorous statistical tests to test for normality which we will cover in future lessons.

# In[6]:

plt.hist(residuals,bins=5)
plt.show()


# # Sum of Squares
# Many of the statistical measures used to evaluate linear regression models rely on three sum of squares measures.The three measures include Sum of Square Error (SSE), Regression Sum of Squares (RSS), and Total Sum of Squares (TSS).In aggregate each of these measures explain the variance of the entire model. We define the measures as the following:
# 
# - We see that SSE is the sum of all residuals giving us a measure between the model's prediction and the observed values. 
# - RSS measures the amount of explained variance which our model accounts for. 
# 
# For instance, if we were to predict every observation as the mean of the observed values then our model would be useless and RSS would be very low. A large RSS and small SSE can be an indicator of a strong model. 
# - TSS measures the total amount of variation within the data.
# 
# With some algebra we can show that TSS=RSS+SSE.

# In[9]:

import numpy as np

SSE = np.sum((yhat - y.values)**2.)
RSS = np.sum((np.mean(y.values)-yhat)**2.)
TSS = np.sum((np.mean(y.values)-y.values)**2)
print SSE,RSS,TSS


# # R-Squared
# The coefficient of determination, also known as R-Squared, is a great measure of linear dependence. It is a single number which tells us what the percentage of variation in the target variable is explained by our model. 
# 
# Intuitively we know that a low SSE and high RSS indicates a good fit. This single measure tells us what percentage of the total variation of the data our model is accounting for.

# In[12]:

R2 = RSS / TSS
print R2


# # Coefficients of the Linear Model

# In[13]:

print linearfit.params


# # Variance of Coefficients
# The variance of each of the coefficients is an important and powerful measure.In our example the coefficient of year represents the number of meters the tower will lean each year. The variance of this coefficient would then give us an interval of the expected movement for each year. 
# 
# In the summary output, next to each coefficient, you see a column with standard errors. The standard error is the square root of the estimated variance. 
# 
# Analyzing the formula term by term we see that the numerator, SSE, represents the error within the model. A small error in the model will then decrease the coefficient's variance. 
# 
# The denomenator term measures the amount of variance within x. A large variance within the independent variable decreases the coefficient's variance.
# 
# Using this variance we will be able to compute t-statistics and confidence intervals regarding this β1.
# 
# 

# In[16]:

SSE = np.sum((y.values - yhat)**2)
xvar = np.sum((pisa.year-pisa.year.mean())**2)
s2b1 = (SSE / float(y.shape[0]-2)) / xvar
print s2b1


# # T-Distribution
# Statistical tests can be done to show that the lean of the tower is dependent on the year.A common test of statistical signficance is the student t-test.
# 
# The t-distribution accounts for the number of observations in our sample set while the normal distribution assumes we have the entire population. In general, the smaller the sample we have the less confidence we have in our estimates. The t-distribution takes this into account by increasing the variance relative to the number of observations. You will see that as the number of observations increases the t-distribution approaches the normal distributions. 
# 
# Scipy has a functions in the library scipy.stats.t which can be used to compute the pdf and cdf of the t-distribution for any number of degrees of freedom. 

# In[18]:

from scipy.stats import t
x = np.linspace(-3,3,100)

print(t.pdf(x=x,df=3))
plt.plot(x,t.pdf(x=x,df=3))
plt.show()


# # Statistical Significance of Coefficients
# To do significance testing we must first start by stating our hypothesis. We want to test whether the lean of the tower depends on the year, ie. every year the tower leans a certain amount.
# 
#  In our case we will say the null hypothesis is that the lean of the tower of pisa does not depend on the year, meaning the coefficient will be equal to zero.
#  
#  Testing the null hypothesis is done by using the t-distribution. The t-statistic is defined as, 
#  
#  This statistic measures how many standard deviations the expected coefficient is from 0. If β1 is far from zero with a low variance then t will be very high. We see from the pdf, a t-statistic far from zero will have a very low probability.

# In[20]:

tstat = linearfit.params['year'] / np.sqrt(s2b1)
print tstat


# # The P-Value
# Finally, now that we've computed the t-statistic we can test our coefficient.we need to find the probability of β1 being different than 0 at some significance level.Lets use the 95% significance level, meaning that we are 95% certian that β1 differs from zero.
# 
# If probability is greater than 0.975 than we can reject the null hypothesis (H0) and say that the year significantly affects the lean of the tower. 

# In[24]:

pval = 0.975

df = pisa.shape[0] - 2

p = t.cdf(tstat,df=df)
if p>pval:
    beta1_test = True
else:
    beta1_test = False

print beta1_test


# # Conclusion
# The assumption of normality is very important in rigorous statistical analysis. This assumption allows each of these statistical tests to be valid. If the assumption is rejected than a different model may be in order. 
# 
# R-squared is a very powerful measure but it is often over used. A low R-squared value does not necessarily mean that there is no dependency between the variables. For instance, if y=sin(x) the r-square would equal 0 but there is certianly a relationship. A high r-squared value does not necessarily mean that the model is good a predicting future events because it does not account for the number of observations seen. 

# In[ ]:



