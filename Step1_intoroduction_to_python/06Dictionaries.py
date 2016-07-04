#coding: UTF-8
#making dictionary
superhero_ranks={} #dictionary
superhero_ranks["Aquaman"] = 1
superhero_ranks["Superman"] = 2
print("dictionary")
print(superhero_ranks)

#indexing a dictionary
president_ranks={}
president_ranks["FDR"] = 1
fdr_rank = president_ranks["FDR"]
print("\nindexing")
print(fdr_rank)

#The in statment and dictionaries
planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}
jupiter_found = "jupiter" in planet_numbers
earth_found = "earth" in planet_numbers
print("\nin statment")
print jupiter_found , earth_found

#Counting with dictionaries
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts = {}
for item in pantry:
    if item in pantry_counts:
        pantry_counts[item] = pantry_counts[item] + 1
    else:
        pantry_counts[item] = 1
print("\ncounting with dictionaies")
print(pantry_counts)

#counting weather
f = open("la_weather.csv")
data = f.read()
data_list = data.split("\n")
weather=[]
for row in data_list:
    weather.append(row.split(","))
weather = weather[1:len(weather)-1]

weather_kind = []
for row in weather:
    weather_kind.append(row[1])

#cout weather start
weather_count = {}
for row in weather_kind:
    if row in weather_count:
        weather_count[row] += 1
    else:
        weather_count[row] = 1
print("\nweather count")
print(weather_count)
