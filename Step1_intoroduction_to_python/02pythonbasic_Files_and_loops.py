#coding: UTF-8
#Opening files
f = open("crime_rates.csv","r")
print(f)
#Reading in files
data = f.read()
print(data)
#Splitting
#stringオブジェクトをsplit()を用いてリストオブジェクトに変換する
rows = data.split("\n")
print(rows[0:5])

#loops
#list of lists
#リストのそれぞれの要素がリストであるようなオブジェクト
final_data =[]
for final in rows:
    final_split = final.split(",")
    final_data.append(final_split)
print(final_data[0:5])

#looping through a list of lists
cities_list = []
for row in final_data:
    cities_list.append(row[0])
print(cities_list[0:5])

int_crime_rates = []
for row in final_data:
    int_crime_rates.append(int(row[1]))
print(int_crime_rates[0:5])
