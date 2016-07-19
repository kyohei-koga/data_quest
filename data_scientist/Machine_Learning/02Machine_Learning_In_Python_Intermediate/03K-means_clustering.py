
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np

nba = pd.read_csv("nba_2013.csv")
nba.head(3)


# # Point Guards
# We are going to focus our lesson on a machine learning technique called clustering, which allows us to visualize the types of point guards as well as group similar point guards together.
# 
# Using 2 features allows us to easily visualize the players and will also make it easier to grasp how clustering works.
# 
# 

# In[2]:

point_guards = nba[nba["pos"] == 'PG']


# # Points Per Game

# In[3]:

point_guards['ppg'] = point_guards['pts'] / point_guards['g']


# # Assist Turnover Ratio

# In[4]:

point_guards = point_guards[point_guards['tov'] != 0]
point_guards['atr'] = point_guards['ast'] / point_guards['tov']


# # Visualizing the Point Guards

# In[5]:

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
plt.scatter(point_guards['ppg'],point_guards['atr'],c='y')
plt.xlabel('Points Per Game',fontsize=13)
plt.ylabel('Assist Turnover Ratio',fontsize=13)
plt.style.use('bmh')
plt.show()


# # Clustering players
# we need to instead use unsupervised machine learning techniques to explore the structure within a data set that doesn't have a clear value to optimize.
# 
# There are multiple ways of clustering data but here we will focus on centroid based clustering for this lesson.
# 
# The key part with K-Means (and most unsupervised machine learning techniques) is that we have to specify what k is. There are advantages and disadvantages to this, but one advantage is that we can pick the k that makes the most sense for our use case.

# # The Algorithm
# Setup K-Means is an iterative algorithm that switches between recalculating the centroid of each cluster and the players that belong to that cluster.To start, select 5 players at random and assign their coordinates as the initial centroids of the just created clusters.
# 
# Step 1 (Assign Points to Clusters) For each player, calculate the Euclidean distance between that player's coordinates, or values for atr & ppg, and each of the centroids' coordinates. Assign the player to the cluster whose centroid is the closest to, or has the lowest Euclidean distance to, the player's values.
# 
# Step 2 (Update New Centroids of the Clusters) For each cluster, compute the new centroid by calculating the arithmetic mean of all of the points (players) in that cluster. We calculate the arithmetic mean by taking the average of all of the X values (atr) and the average of all of the Y values (ppg) of the points in that cluster.
# 
# 
# 

# In[6]:

num_clusters = 5
random_initial_points = np.random.choice(point_guards.index,size=num_clusters)
centroids = point_guards.ix[random_initial_points]


# # Visualize Centroids

# In[7]:

plt.scatter(point_guards['ppg'],point_guards['atr'],c='y')
plt.scatter(centroids['ppg'],centroids['atr'],c='r')
plt.title('Centroids')
plt.xlabel('Points Per Game',fontsize=13)
plt.ylabel('Assist Turnover Ratio',fontsize=13)
plt.show()


# # Setup (continued)
# Moving forward, let's use a dictionary object instead to represent the centroids.
# 
# We will need a unique identifier, like cluster_id, to refer to each cluster's centroid and a list representation of the centroid's coordinates (or values for ppg and atr). 
# 
# To generate the cluster_ids, let's iterate through each centroid and assign an integer from 0 to k-1. For example, the first centroid will have a cluster_id of 0, while the second one will have a cluster_id of 1.
# 
# 

# In[18]:

def centroids_to_dict(centroids):
    dictionary = dict()
    counter = 0
    
    for index,row in centroids.iterrows():
        coordinates = [row['ppg'],row['atr']]
        dictionary[counter] =coordinates
        counter += 1
        
    return dictionary

centroids_dict = centroids_to_dict(centroids)


# # Step 1 (Euclidean Distance)
# While in higher dimensions, Euclidean distance can be misleading, in 2 dimensions Euclidean distance is essentially the Pythagorean theorem. 

# In[19]:

import math

def calculate_distance(centroid,player_values):
    root_distance = 0
    
    for x in range(0,len(centroid)):
        difference = centroid[x] - player_values[x]
        squared_difference = difference ** 2
        root_distance += squared_difference
    
    euclid_distance = math.sqrt(root_distance)
    return euclid_distance

q = [5,2]
p = [3,1]

print(calculate_distance(q,p))


# # Step 1 (Continued)
# Now we need a way to assign data points to clusters based on Euclidean distance. Instead of creating a new variable or data structure to house the clusters, let's keep things simple and just add a column to the point_guards data frame that contains the cluster_id of the cluster it belongs to.

# In[20]:

def assign_to_cluster(row):
    lowest_distance = -1
    closest_cluster = -1
    
    for cluster_id,centroid in centroids_dict.items():
        df_row = [row['ppg'],row['atr']] #position
        euclidean_distance = calculate_distance(centroid,df_row) #calculate distance
        
        if lowest_distance == -1:
            lowest_distance = euclidean_distance
            closest_cluster = cluster_id
        elif euclidean_distance < lowest_distance:
            lowest_distance = euclidean_distance
            closest_cluster = cluster_id
    
    return closest_cluster

point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row),axis=1)


# # Visualizing Clusters
# Let's write a function, visualize_clusters, that we can use to visualize the clusters easily.

# In[21]:

def visualize_clusters(df,num_clusters):
    colors = ['b','g','r','c','m','y','k']
    
    for n in range(num_clusters):
        clustered_df = df[df['cluster'] == n]
        plt.scatter(clustered_df['ppg'],clustered_df['atr'],c=colors[n-1])
    plt.xlabel('Points Per Game',fontsize=13)
    plt.ylabel('Assist Turnover Ratio',fontsize=13)
    plt.show()
    
visualize_clusters(point_guards,5)


# # Step 2
# Now let's code Step 2, where we recalculate the centroids for each cluster.

# In[25]:

def recalculate_centroids(df):
    new_centroids_dict = dict()
    
    for cluster_id in range(0,num_clusters):
        values_in_cluster = df[df['cluster'] == cluster_id]
        new_centroid = [np.average(values_in_cluster['ppg']),
                         np.average(values_in_cluster['atr'])]
        new_centroids_dict[cluster_id] = new_centroid
    return new_centroids_dict

centroids_dict = recalculate_centroids(point_guards)


# # Repeat Step 1
# Now that we recalculated the centroids, let's re-run Step 1 (assign_to_cluster) and see how the clusters shifted.

# In[26]:

point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row),axis=1)
visualize_clusters(point_guards,num_clusters)


# # Repeat Step 2 and Step 1
# Now we need to recalculate the centroids, and shift the clusters again.

# In[27]:

centroids_dict = recalculate_centroids(point_guards)
point_guards['cluster'] = point_guards.apply(lambda row:assign_to_cluster(row),axis=1)
visualize_clusters(point_guards,num_clusters)


# # Challenges of K-Means
# the clusters visually look like they don't move a lot after every iteration. This means 2 things:
# - K-Means doesn't cause massive changes in the makeup of clusters between iterations, meaning that it will always converge and become stable
# - Because K-Means is conservative between iterations, where we pick the initial centroids and how we assign the players to clusters initially matters a lot
# 
# To counteract these problems, the sklearn implementation of K-Means does some intelligent things like re-running the entire clustering process lots of times with random initial centroids so the final results are a little less biased on one passthrough's initial centroids.

# In[30]:

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(point_guards[['ppg','atr']])
point_guards['cluster'] = kmeans.labels_

visualize_clusters(point_guards,num_clusters)

