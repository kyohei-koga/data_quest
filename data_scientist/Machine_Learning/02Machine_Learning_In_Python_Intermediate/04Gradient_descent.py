
# coding: utf-8

# For many machine learning algorithms it's important to scale, or normalize, the data before using it.These two fields are on very different scales which can produce bias into learning algorithms.

# In[14]:

import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

pga = pd.read_csv('pga.csv')

pga.distance = (pga.distance - pga.distance.mean()) / pga.distance.std()
pga.accuracy = (pga.accuracy - pga.accuracy.mean()) / pga.accuracy.std()

plt.scatter(pga.distance,pga.accuracy)
plt.xlabel('normalized distance')
plt.ylabel('normalized accuracy')
plt.style.use('fivethirtyeight')
plt.show()


# # Linear model
# We can use a linear model, as shown in previous missions, to model this data. This model is written as $$accuracy_i=\theta_1 distance_i + \theta_0 + \epsilon_i$$where θ's are coefficients and ϵ are error terms.

# In[68]:

from sklearn.linear_model import LinearRegression
import numpy as np

print 'shape of the series: %s' %pga.distance.shape
print 'Shape with newaxis: %d,%d' %pga.distance[:,np.newaxis].shape

# The X variable in LinearRegression.fit() must have 2 dimensions
model = LinearRegression()
model.fit(pga.distance[:,np.newaxis],pga.accuracy)
theta1 = model.coef_[0]
print theta1


# # Cost function, introduction
# Least squares is a method which directly minimized the sum of square error in a model algebraically. Often times we have too much data to fit into memory and we can't use least squares. 
# 
# Gradient descent is a general method that can be used to estimate coefficents of nearly any model, including linear models. At it's core, gradient descent minimizes the residuals in the estimated model by updating each coefficent based on it's gradient. 
# 
# To start we must understand cost functions. Most cost functions measure the difference between a model predictions and it's corresponding observations with the coefficients as parameters. Lets say our model is hθ(x)=θ1x+θ0. 
# 
# The cost function is then defined as,$$J(\theta_0, \theta_1) = \dfrac{1}{2m} \sum_{i=1}^m (h_{\theta}(x_i) - y_i)^2$$
# 
#  As we change the coefficients of the model this cost changes. During modeling we will randomly choose the coefficients and update them intelligently to minimize this cost.

# In[72]:

def cost(theta0,theta1,x,y):
    J = 0
    #the number of observations
    m = len(x)
    #loop therough each obseravations
    for i in range(m):
        h = theta1 * x[i] + theta0
        J += (h-y[i]) ** 2
    J /= 2*m
    return J

print cost(0,1,pga.distance,pga.accuracy)

theta0 = 100
theta1s = np.linspace(-3,2,100)
costs = []
for theta1 in theta1s:
    costs.append(cost(theta0,theta1,pga.distance,pga.accuracy))

plt.plot(theta1s,costs,c='r')
plt.style.use('bmh')
plt.show()    
    


# # Cost function, continued
# The cost function above is quadratic, like a parabola, with respect to the slope and we can see there is a global minimum.
# 
# We need to find the best set of parameters to minimize the cost function, but here we are only varying the slope and keeping the intercept constant. The minimum of the cost function is the point where the model has the lowest error, hence the point where our parameters are optimized. Instead we can use a 3D plot to visualize this cost function where the x and y axis will be the slope and intercept and the z axis will be the cost.

# In[84]:

from mpl_toolkits.mplot3d import Axes3D
#Exmaple of a surface plot using matplotlib
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)

#we must create variables to represent each possible pair of points in x and y.
#ie. (-10,-10),(-10,-9.8),...(0,0),...,(10,9.8),(10,10)
#x and y need to be transformed to 100☓100 matrices to represent these coodinates
X,Y = np.meshgrid(x,y) #Xは列方向に、Yは行方向に値を変化させる
print X[:5,:5]
print Y[:5,:5]

Z = X**2 + Y**2

fig = plt.figure()
# Initialize 3D plot
ax = fig.gca(projection='3d')
ax.plot_surface(X=X,Y=Y,Z=Z)
plt.show()

theta0s = np.linspace(-2,2,100)
theta1s = np.linspace(-2,2,100)
COST = np.empty(shape=(100,100))

X,Y = np.meshgrid(theta0s,theta1s)

for i in range(100):
    for j in range(100):
        COST[j,i] = cost(X[0,i],Y[j,0],pga.distance,pga.accuracy)
fig2 = plt.figure()
ax = fig2.gca(projection='3d')
ax.plot_surface(X=X,Y=Y,Z=COST)
plt.show()


# # Cost function, slopes
# Gradient descent relies on finding the direction of the largest gradient where a gradient is the "slope" of a multivariable function.To find this gradient we can take the partial derivative in terms of each parameter in the cost function.
# ie. holding all other variables constant, what is the slope in the direction of the one parameter. In the case of this cost function, we will take the partial derivatives in terms of theta0 and theta1.
# $$\dfrac{\partial J(\theta_0, \theta_1)}{\partial \theta_0}$$
# is read as the partial derivative of J(θ0,θ1) in terms of θ0. This is not part of the equation but just the representation of partial derivatives. 
# 
# The partial derivative of the cost function in terms of theta0 is: 
# $$\dfrac{\partial J(\theta_0, \theta_1)}{\partial \theta_0} = \dfrac{1}{m} \sum_{i=1}^m (h_{\theta}(x_i)-y_i)$$
# 
# The partial deriviate of the cost function in terms of theta1 is:
# $$\dfrac{\partial J(\theta_1)}{\partial \theta_1} = \dfrac{1}{m} \sum_{i=1}^m (h_{\theta}(x_i)-y_i) * x_i$$
# 
# This function gives us the slope in the direction of the θ1 coefficient.

# In[89]:

def partial_cost_theta1(theta0,theta1,x,y):
    h = theta0 + theta1*x
    diff = (h - y) * x
    partial = diff.sum() / float(x.shape[0])
    return partial
partial1 = partial_cost_theta1(0,5,pga.distance,pga.accuracy)
print('paratial1=%f' %partial1)

def partial_cost_theta0(theta0,theta1,x,y):
    h = theta0 + theta1*x
    diff = (h - y)
    partial = diff.sum() / float(x.shape[0])
    return partial
partial0 = partial_cost_theta0(1,1,pga.distance,pga.accuracy)
print('paratial0=%f' %partial0)


# # Gradient descent algorithm
#  In order to minimize the error between our hypothesised model and observations we can find the minimum of the cost function by changing the parameters.
#  
#   To execute gradient descent we randomly initialize a set of parameters and update them by moving in the direction of the cost function's steepest slope, ie. the descending down the function.
#   
#   Eventually the updates will converge to a near optimal set of parameters. When parameters converge the hypothesised parameters become very close to the optimal parameters. We measure convergence by finding the difference between the previous iterations cost versus the current cost.
#   The general gradient descent algorithm for two variables is:
# $$\theta_1 := \theta_1 - \alpha * \dfrac{\partial J(\theta_0, \theta_1)}{\partial \theta_0}$$
# $$\theta_0 := \theta_0 - \alpha * \dfrac{\partial J(\theta_0, \theta_1)}{\partial \theta_1}$$repeat until convergence.
# 
# Let's go through this term by term. θ1 is the current value of our coefficient, ie. how much accuracy is lost per yard of distance. α is the learning rate. This value is set by the user and controls how fast the algorithm will converge by changing the parameters by some percentage of the slope.
# 
#  Values of this learning rate can vary from project to project but in general learning rates can be between 0.0001 and 1. This value must not be too large or the algorithm will overshoot the minimum but if it's too small it will take many iterations to converge.
#  
#  A good starting point is 0.01. If you find that the algorithm is learning too slowly it can be increased. If the cost starts increasing out of control then the learning rate is probably overshooting the minimum and should be decreased.

# In[93]:

#x is our feature vector -- distance
#y is our target variable -- accuracy
#alpha is the learning rate
#theta0 is the initial theta0
#theta1 is the initial theta1
def gradient_descent(x,y,alpha=0.1,theta0=0,theta1=0):
    max_epochs = 1000
    counter = 0 #initialize counter
    c = cost(theta1,theta0,pga.distance,pga.accuracy) ## initial cost
    costs = [c] #Lets store each updates
    #must set a convergence thereshold to find where the cost function in minimized
    #when the difference between the previous cost and current cost is less than this value we will say the parameters have converged
    convergence_thres = 0.000001
    cprev = c + 10 # initialize
    theta0s = [theta0]
    theta1s = [theta1]
    # When the costs converge or we hit a large number of iterations will we stop updating
    while (np.abs(cprev - c) > convergence_thres) and (counter < max_epochs):
        cprev = c
        updata0 = alpha * partial_cost_theta0(theta0,theta1,x,y)
        updata1 = alpha * partial_cost_theta1(theta0,theta1,x,y)
        #update theta0 and theta1 at the same time
        #we want to compute the slopes at the same set of hypothesised parameters
        #so we update after finding the partial delivatives
        theta0 -= updata0
        theta1 -= updata1
        
        #store thetas
        theta0s.append(theta0)
        theta1s.append(theta1)
        
        #compute the new cost
        c = cost(theta0,theta1,pga.distance,pga.accuracy)
        
        #store updates
        costs.append(c)
        counter += 1
    
    return {'theta0':theta0s,'theta1':theta1s,'costs':costs}

print("Theta1 =", gradient_descent(pga.distance, pga.accuracy)['theta1'])
data = gradient_descent(pga.distance,pga.accuracy,alpha=0.01)
plt.plot(range(len(data['costs'])),data['costs'])


# In[ ]:



