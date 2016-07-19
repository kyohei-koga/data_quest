
# coding: utf-8

# # Neural Networks And Iris Flowers
# Many machine learning prediction problems are rooted in complex data and its non-linear relationships between features. Neural networks are a class of models that can learn these non-linear interactions between variables.

# In[17]:

get_ipython().magic(u'matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

names = ['sepal_length','sepal_width','petal_length','petal_width','species']
iris = pd.read_csv("iris.data",names=names)

shuffled_rows = np.random.permutation(iris.index)
iris = iris.iloc[shuffled_rows,:]

print(iris.head(2))

iris.hist()
plt.show()


# # Neurons
# So far we have talked about methods which do not allow for a large amount of non-linearity.
# 図
# 
# Neither a linear model nor logistic model is capable of building such a function, so we must explore other options like neural networks. 
# 
# Neural networks are very loosely inspired by the structure of neurons in the human brain. These models are built by using a series of activation units, known as neurons, to make predictions of some outcome. Neurons take in some input, apply a transformation function, and return an output. Below we see a representation of a neuron. 図
# 
# This neuron is taking in 5 units represented as x, a bias unit, and 4 features. This bias unit (1) is similar in concept to the intercept in linear regression and it will shift the activity of the neuron to one direction or the other. These units are then fed into an activation function h. We will use the popular sigmoid (logistic) activation function because it returns values between 0 and 1 and can be treated as probabilities. 
# 
# $$\text{Sigmoid Function: }g(z) = \dfrac{1}{1 + e^{-z}}$$
# 
# This sigmoid function then leads to the corresponding activation function: 
# 
# $$\text{Sigmoid Activation Function: }h_{\Theta}(x) = \dfrac{1}{1+e^{-\Theta^T x}} = \dfrac{1}{1+e^{-(\theta_01 + \theta_1x_1 + \theta_2 x_2)}}$$
# 
# If you look closely, you might notice that the logistic regression function we learned in previous lessons can be represented here as a neuron.

# In[32]:

z = np.asarray([[9,5,4]])
y = np.asarray([[-1,2,4]])

#np.dot is used for matrix multiplication
print(np.dot(z,y.T))

iris['ones'] = np.ones(iris.shape[0])
X = iris[['ones','sepal_length','sepal_width','petal_length','petal_width']].values
y = (iris.species == 'Iris-versicolor').values.astype(int)

x0 = X[0]

theta_init = np.random.normal(0,0.01,size=(5,1))

def sigmoid_activation(x,theta):
    x = np.asarray(x)
    theta = np.asarray(theta)
    return 1. / (1. + np.exp(-np.dot(theta.T,x)))

a1 = sigmoid_activation(x0,theta_init)
print a1


# In[39]:

print theta_init.T


# # Cost function
# We can train a single neuron as a two layer network using gradient descent. The cost function measures the difference between the desired output and actual output, defined as: 
# 
# $$J(\Theta) = -\dfrac{1}{m} \sum_{i=1}^{m} (y_i * log(h_{\Theta}(x_i)) + (1-y_i) log(1-h_{\Theta}(x_i)))$$
# 
# Since our targets, yi, are binary, either yi or (1−yi) will equal zero. One of the terms in the summation will disappear because of this result and.the activation function is then used to compute the error. 

# In[71]:

x0 = X[0]
y0 = y[0]

#initialize parametrs, we have 5 units and just 1 layer
theta_init = np.random.normal(0,0.01,size=(5,1))

def singlecost(X,y,theta):
    h = sigmoid_activation(X.T,theta)
    cal = -np.mean(y*np.log(h) + (1-y)*np.log(1-h))
    return cal

first_cost = singlecost(x0,y0,theta_init)


# # Compute the Gradients
#  Calculating derivatives are more complicated in neural networks than in linear regression. Here we must compute the overall error and then distribute that error to each parameter. Compute the derivative using the chain rule.
#  
#  $$\dfrac{\partial J}{\partial \theta_j} = \dfrac{\partial J}{\partial h(\Theta)} \dfrac{\partial h(\Theta)}{\partial \theta_j}$$
#  
#  The first part is computing the error between the target variable and prediction.The second part then computes the sensitivity relative to each parameter. In the end, the gradients are computed as:
#  
#  $$\delta = (y_i - h_\Theta(x_i)) * h_\Theta(x_i) * (1-h_\Theta(x_i)) * x_i$$
#  
#  Now we will step through the math. (yi−hΘ(xi)) is a scalar and the error between our target and prediction. hΘ(xi)∗(1−hΘ(xi)) is also a scalar and the sensitivity of the activation function. xi is the features for our observation i.δ is then a vector of length 5, 4 features plus a bias unit, corresponding to the gradients. 
#  
#  To implement this, we compute δ for each observation, then average to get the average gradient. The average gradient is then used to update the corresponding parameters.

# In[72]:

theta_init = np.random.normal(0,0.01,size=(5,1))

#store the updates into this array
grads = np.zeros(theta_init.shape)

n = X.shape[0]
for j,obs in enumerate(X):
    #compute activation
    h = sigmoid_activation(obs,theta_init)
    delta = (y[j] - h) * h * (1-h) * obs
    #accumulate
    grads += delta[:,np.newaxis] / X.shape[0]


# # Two layer network
# Now that you can compute the gradients, use gradient descent to learn the parameters and predict the species of iris flower given the 4 features.  Gradient descent minimizes the cost function by adjusting the parameters accordingly. Adjust the parameters by substracting the product of the gradients and the learning rate from the previous parameters. Repeat until the cost function coverges or a maximum number of iterations is reached. 

# In[76]:

theta_init = np.random.normal(0,0.01,size=(5,1))

#set a learning rate
learning_rate = 0.1
# maximum number of iterations for gradient descent
maxepochs = 10000
# costs convergence threshold
convergence_thres = 0.0001

def learn(X,y,theta,learning_rate,maxepochs,convergence_thres):
    costs = []
    cost = singlecost(X,y,theta) #compute initial cost
    costprev = cost + convergence_thres + 0.01 #set an initial costprev to past while loop
    counter = 0
    #loop through until convergence
    for counter in range(maxepochs):
        grads = np.zeros(theta.shape)
        for j,obs in enumerate(X):
            h = sigmoid_activation(obs,theta_init)
            delta = (y[j]-h)*h*(1-h)*obs
            grads += delta[:,np.newaxis] / float(X.shape[0])
        
        #update parameters
        theta += grads * learning_rate
        counter += 1
        costprev = cost
        cost = singlecost(X,y,theta)
        costs.append(cost)
        if np.abs(costprev - cost) < convergence_thres:
            break

    plt.plot(costs)
    plt.title('Convergence of the Cost Function')
    plt.ylabel('J($\Theta$)')
    plt.xlabel('Iteration')
    plt.show()
    return theta

theta = learn(X,y,theta_init,learning_rate,maxepochs,convergence_thres)


# # Neural Network
# Neural networks are usually built using mulitple layers of neurons.Adding more layers into the network allows you to learn more complex functions. Here's a picture representing a 3 layer neural network.図
# 
# We have a 3 layer neural network with four input variables x1,x2,x3, and x4 and a bias unit. Each variable and bias unit is then sent to four hidden units, a(2)1,a(2)2,a(2)3, and a(2)4. The hidden units have different sets of parameters θ. 
# 
# $$a_1^{(2)} = g(\theta_{1,0}^{(1)} + \theta_{1,1}^{(1)} x_1 + \theta_{1,2}^{(1)} x_2 + \theta_{1,3}^{(1)} x_3 + \theta_{1,4}^{(1)} x_4)$$
# $$a_2^{(2)} = g(\theta_{2,0}^{(1)} + \theta_{2,1}^{(1)} x_1 + \theta_{2,2}^{(1)} x_2 + \theta_{2,3}^{(1)} x_3 + \theta_{2,4}^{(1)} x_4)$$
# $$a_3^{(2)} = g(\theta_{3,0}^{(1)} + \theta_{3,1}^{(1)} x_1 + \theta_{3,2}^{(1)} x_2 + \theta_{3,3}^{(1)} x_3 + \theta_{3,4}^{(1)} x_4)$$
# $$a_4^{(2)} = g(\theta_{4,0}^{(1)} + \theta_{4,1}^{(1)} x_1 + \theta_{4,2}^{(1)} x_2 + \theta_{4,3}^{(1)} x_3 + \theta_{4,4}^{(1)} x_4)$$
# 
# θ(j)i,k represents the parameter of input unit k which transform the units in layer j to activation unit a(j+1)i.
# 
# This layer is known as a hidden layer because the user does not directly interact with it by passing or retrieving data. The third and final layer is the output, or prediction, of our model. Similar to how each variable was sent to each neuron in the hidden layer, the activation units in each neuron are then sent to each neuron on the next layer. Since there is only a single layer, we can write it as: 
# 
# $$h_{\Theta}(X) = g(\theta_{1,0}^{(2)} + \theta_{1,1}^{(2)} a_1^{(2)} + \theta_{1,2}^{(2)} a_2^{(2)} + \theta_{1,3}^{(2)} a_3^{(2)} + \theta_{1,4}^{(2)} a_4^{(2)})$$
# 
# While the mathematical notation may seem confusing at first, at a high level, we are organizing multiple logistic regression models to create a more complex function.

# In[81]:

theta0_init = np.random.normal(0,0.01,size=(5,4))
theta1_init = np.random.normal(0,0.01,size=(5,1))
def feedforward(X,theta0,theta1):
    #feedforward to the first layer
    a1 = sigmoid_activation(X.T,theta0).T
    #add a column of ones for bias term
    a1 = np.column_stack([np.ones(a1.shape[0]),a1])
    #activation units are then inputted to the output layer
    out = sigmoid_activation(a1.T,theta1)
    return out

h = feedforward(X,theta0_init,theta1_init)


# # Multiple neural network cost function
# The cost function to multiple layer neural networks is identical to the cost function we used in the last screen, but hΘ(xi) is more complicated. 
# 
# $$J(\Theta) = -\dfrac{1}{m} \sum_{i=1}^m (y_{i} * log(h_{\Theta}(x_{i}))  +  (1-y_{i}) log(1-h_{\Theta}(x_i))$$

# In[83]:

theta0_init = np.random.normal(0,0.01,size=(5,4))
theta1_init = np.random.normal(0,0.01,size=(5,1))

#X and y are in memory and should be used as inputs to multipltcost()
def multiplecost(X,theta0,theta1):
    h = feedforward(X,theta0,theta1)
    inner = (y * np.log(h)) + (1-y) * np.log(1-h)
    return -np.mean(inner)

c = multiplecost(X,theta0_init,theta1_init)


# # Backpropagation
# Now that we have mulitple layers of parameters to learn, we must implement a method called backpropagation.We've already implemented forward propagation by feeding the data through each layer and returning an output. 
# Backpropagation focuses on updating parameters starting at the last layer and circling back through each layer, updating accordingly. As there are multiple layers we are forced to compute $$\dfrac{\partial}{\partial \Theta_{i,j}^{(l)}} J(\Theta)$$ where l is the layer. For a three layer network, use the following approach, $$\delta_j^l \text{ is the 'error' for unit j in layer l}$$
# 
# $$\delta^3 = h_\Theta(X) - y$$
# $$\delta^2 = (\Theta^{(2)})^T \delta^3 .* g^{'}(z^{(2)})$$
# $$\text{There is no } \delta^1 \text{ since the first layer are the features and have no error.}$$
# 
#  You will notice that there are many parameters and moving parts to this algorithm. To make the code more modular, we have refactored our previous code as a class, allowing us to organize related attributes and methods.

# In[99]:

class NNet3:
    def __init__(self,learning_rate=0.5,maxepochs=1e4,convergence_thres=1e-5,hidden_layer=4):
        self.learning_rate = learning_rate
        self.maxepochs = int(maxepochs)
        self.convergence_thres = 1e-5
        self.hidden_layer = int(hidden_layer)
        
    def _multiplecost(self,X,y):
        #feed through network
        l1,l2 = self._feedforward(X)
        # compute error
        inner = y*np.log(l2) + (1-y)*np.log(1-l2)
        # neggative of average error
        return -np.mean(inner)
    
    def _feedforward(self,X):
        # feedforward to the first_layer
        l1 = sigmoid_activation(X.T,self.theta0).T
        #add a column of ones for bias
        l1 = np.column_stack([np.ones(l1.shape[0]),l1])
        # acctivation inits are then inputted to the output layer
        l2 = sigmoid_activation(l1.T,self.theta1)
        return l1,l2
    
    def predict(self,X):
        _,y = self._feedforward(X)
        return y
    
    def learn(self,X,y):
        nobs,ncols = X.shape
        self.theta0 = np.random.normal(0,0.01,size=(ncols,self.hidden_layer))
        self.theta1 = np.random.normal(0,0.01,size=(self.hidden_layer+1,1))
        
        self.costs = []
        cost = self._multiplecost(X,y)
        self.costs.append(cost)
        costprev = cost + self.convergence_thres+1 #set an initial costprev to past while loop
        counter = 0
        
        for counter in range(self.maxepochs):
            l1,l2 = self._feedforward(X)
            
            #start backpropagation
            #compute gradients
            l2_delta = (y-l2)*l2*(1-l2)
            l1_delta = l2_delta.T.dot(self.theta1.T) * l1 * (1-l1)
            
            #Update parameters by averaging gradients and multiplying by the learning rate
            self.theta1 += (l1.T.dot(l2_delta.T) / nobs)*self.learning_rate
            self.theta0 += (X.T.dot(l1_delta)[:,1:] / nobs)*self.learning_rate
            
            #store costs and check for convergence
            counter += 1
            costprev = cost
            cost = self._multiplecost(X,y)
            self.costs.append(cost)
            if np.abs(costprev-cost) < self.convergence_thres and counter > 500:
                break
    
learning_rate = 0.5
maxepochs = 10000
convergence_thres = 0.00001
hidden_units = 4

#initialize model
model = NNet3(learning_rate=learning_rate,
              maxepochs=maxepochs,
              convergence_thres=convergence_thres,
              hidden_layer=hidden_units)
model.learn(X,y)

plt.plot(model.costs)
plt.title("Convergence of the Cost Function")
plt.ylabel("J($\Theta$)")
plt.xlabel("Iteration")
plt.show()


# # Splitting data
# Now that we have learned about neural networks, learned about backpropagation, and have code which will train a 3-layer neural network, we will split the data into training and test datasets and run the model.

# In[100]:

# First 70 rows to X_train and y_train
# Last 30 rows to X_train and y_train
X_train = X[:70]
y_train = y[:70]

X_test = X[-30:]
y_test = y[-30:]


# # Predicting iris flowers
# To benchmark how well a three layer neural network performs when predicting the species of iris flowers, you will have to compute the AUC, area under the curve, score of the receiver operating characteristic. The function NNet3 not only trains the model but also returns the predictions.

# In[105]:

from sklearn.metrics import roc_auc_score
# Set a learning rate
learning_rate = 0.5
# Maximum number of iterations for gradient descent
maxepochs = 10000       
# Costs convergence threshold, ie. (prevcost - cost) > convergence_thres
convergence_thres = 0.00001  
# Number of hidden units
hidden_units = 4

# Initialize model 
model = NNet3(learning_rate=learning_rate, maxepochs=maxepochs,
              convergence_thres=convergence_thres, hidden_layer=hidden_units)
model.learn(X_train,y_train)
yhat = model.predict(X_test)[0]

auc = roc_auc_score(y_test,yhat)
print auc

