# coding: UTF-8
f = open("la_weather.csv","r")
data = f.read()
data_split = data.split("\n")
weather_data=[]
for row in data_split:
    new_row = row.split(",")
    weather_data.append(new_row)
weather_data=weather_data[1:len(weather_data)-1]
print(weather_data[:])
#getting a single column
weather = []
for row in weather_data:
    weather.append(row[1])
print(weather[:5])
#in statment retuen retuen Boolean
#weather_typesを含むかふくまないか
weather_type_found=[]
weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
for row in weather_types:
    found = (row in weather)
    weather_type_found.append(found)
print(weather_type_found)
