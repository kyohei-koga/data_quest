#coding: UTF-8
import requests
import json
import csv

response = requests.get("http://api.nal.usda.gov/ndb/reports/?ndbno=01001&type=b&format=json&api_key=DEMO_KEY")
#print(response.status_code)
#print(response.headers)
#print(response.headers['Content-Type'])
#print(response.json())
data = response.json()
print(data['report']['food']['ndbno'])
print(data['report']['food'])
print(data['report']['food']['nutrients'][0]['name'])
print(data['report']['food']['nutrients'][0]['value'])
print(data['report']['food']['nutrients'][1]['name'])
print(data['report']['food']['nutrients'][1]['value'])
print(data['report']['food']['nutrients'][2]['name'])
print(data['report']['food']['nutrients'][2]['value'])
print(data['report']['food']['nutrients'][31]['name'])
print(data['report']['food']['nutrients'][31]['value'])

#f = open('sample.csv','w')
#writer = csv.writer(f,lineterminator='\n')

sample_name =[]
sample_value = []
for row in data['report']['food']['nutrients']:
    sample_name.append(row['name'])
    sample_value.append(row['nutrient_id'])
#sample = [sample_name,sample_value]
#sample.append(sample_value)
print(sample_name)
print(sample_value)
#writer.writerows(sample)
#f.close
