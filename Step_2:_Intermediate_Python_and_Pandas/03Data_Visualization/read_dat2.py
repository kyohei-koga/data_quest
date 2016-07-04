#coding: UTF-8

import pandas as pd
names = ['id','name','city','country','iata/faa','icao','latitude','longitude','altitude','timezone','dst','tz_database_time_zone']
airports = pd.read_csv("airports.dat",header=None,names=names)
airports.to_csv('airports.csv',index=False)

names =  ['id','name','alias','iata','icao','callsign','country','active']
airlines = pd.read_csv("airlines.dat",header=None,names=names)
airlines.to_csv('airlines.csv',index=False)

names = ['airline','id','source_airport','source_airport_id','destination_airport','destination_airport_id','codeshare','stops','equipment']
routes = pd.read_csv("routes.dat",header=None,names=names)
routes.to_csv('routes.csv',index=False)
