#coding: UTF-8
import requests
import json
import csv
offset_no = [0,1500,3000,4500,6000,7500]
f = open('sample.csv','w')
writer = csv.writer(f,lineterminator='\n')
header = ["NDO_No","Shrt_Desc","Cholestrl_(mg)","Protein_(g)","Energ_Kcal","Water_(g)"]
writer.writerow(header)

for row in offset_no:
    response = requests.get("http://api.nal.usda.gov/ndb/nutrients/?format=json&api_key=DEMO_KEY&nutrients=255&nutrients=208&nutrients=203&nutrients=601&max=1500&offset=%s" %row)
    data = response.json()
    sample = []
    for row in data['report']['foods']:
        name_convert = row['name'].replace(',','')
        name_convert = name_convert.replace(';','')
        sample.append([row['ndbno'],name_convert,row['nutrients'][0]['gm'],row['nutrients'][1]['gm'],row['nutrients'][2]['gm'],row['nutrients'][3]['gm']])
    writer.writerows(sample)

f.close
