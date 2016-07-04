#coding: UTF-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.basemap import Basemap

airlines = pd.read_csv('airlines.csv')
airports = pd.read_csv('airports.csv')
routes = pd.read_csv('routes.csv')

sampler = np.random.permutation(len(airports))
sampled = airports.take(sampler)
sampled.index = [i for i in range(len(sampled))]
print(sampled)
airports['end_lat'] = sampled['latitude']
airports['end_lon'] = sampled['longitude']
#Geographic coordinate systems
#latitude and longitude values describe points on a sphere, we need to convert them to x and y coordinates so we can plot them on a 2D map.

#Basemap
#The matplotlib basemap toolkit is a library for plotting 2D data on maps in Python. Basemap does not do any plotting on it’s own,
#but provides the facilities to transform csian coordinates using the Basemap instance.
#    Use the Matplotlib and Basemap methods to customize the map.
#    Use the show() method from Matplotlib to display the map.
#Let's focus on the first step and create a new Basemap instance.
#m = Basemap(projection="merc")
#The following parameters are required:
#    projection - the map projection.
#    llcrnrlat - latitude of lower left hand corner of the desired map domain (degrees).
#    urcrnrlat - latitude of upper right hand corner of the desired map domain (degrees).
#    llcrnrlon - longitude of lower left hand corner of the desired map domain (degrees).
#    urcrnrlon- longitude of upper right hand corner of the desired map domain (degrees).

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)

#Converting from spherical to cartesian coordinates
#You can pass in a List of latitude and longitude values into the Basemap instance and it will return back
#a converted list of latitude and longitude values using the projection you specified earlier

#convert to list object
longitudes = airports['longitude'].tolist()
latitudes = airports['latitude'].tolist()
#convert latitude and longitude to x and y coordinates
x,y = m(longitudes,latitudes)

#Generating a scatter plot
#use the the Basemap method scatter().
#m.scatter(x,y)
#s parameter is size of dot
plt.scatter(x,y,s=1)
plt.show()

#Customizing the plot using Basemap
#To display the coast lines, you can use the drawcoastlines() method.
m.scatter(x,y,s=1)
m.drawcoastlines()#Iterate over DataFrame rows as (index, Series) pairs.#create figure instance
fig = plt.figure(figsize=(15,20))
ax = fig.add_subplot(1,1,1)
ax.set_title("Scaled up Earth with Coastlines")
m.scatter(x,y,s=1)
m.drawcoastlines()
plt.show()

#Displaying great circles
#To better understand the flight routes, we can draw great circles to connect starting and ending locations on a map.
#A great circle is the shortest circle connecting 2 points on a sphere.
#We use the Basemap method drawgreatcircle() to display a great circle between 2 points. The drawgreatcircle() method requires 4 parameters in the following order:
#    lon1 - longitude of the starting point.
#    lat1 - latitude of the starting point.
#    lon2 - longitude of the ending point.
#    lat2 - latitude of the ending point.
#You'll notice that great circles aren't created for routes that differ by more than 180 degrees in either latitude or longitude.
#This is because the drawgreatcircle() method isn't able to create great circles properly when they go outside of the map boundaries.

fig = plt.figure(figsize=(15,20))
m.drawcoastlines()

def create_great_circles(df):
    for index,row in df.iterrows():#Iterate over DataFrame rows as (index, Series) pairs.
        start_lon = row['longitude']
        start_lat = row['latitude']
        end_lon = row['end_lon']
        end_lat = row['end_lat']

        if abs(end_lat - start_lat) < 180 and abs(end_lon - start_lon) < 180:
            m.drawgreatcircle(start_lon,start_lat,end_lon,end_lat ,linewidth=1)
USA = airports[airports['country'] == 'Namib']
create_great_circles(USA)
plt.show()
