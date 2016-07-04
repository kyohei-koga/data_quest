#coding: UTF-8
#Enumerate
#There are many times when we'll need to iterate over multiple lists in tandem

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
for i,ship in enumerate(ships):
    print(ships[i])
    print(cars[i])

things = [["apple","monkey"],["orange","dog"],["banana","cat"]]
trees = ["cedar","maple","fig"]

for i, thing in enumerate(things):
    thing.append(trees[i])

print(things)

#List comprehension
apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [price * 2 for price in apple_prices]
apple_prices_lowered = [price - 100 for price in apple_prices]

print(apple_prices_doubled,apple_prices_lowered)

import csv
f = open("legislators.csv")
legislators = csv.reader(f)
legislators = list(legislators)
name_counts = {}
#birthday convert to year(type is int)
for row in legislators:
    year = row[2].split("-")
    try:
        year[0] = int(year[0])
    except:
        year[0] = 1
    row.append(year[0])

for row in legislators:
    if row[3] == "M" and row[7] > 1700:
        name = row[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
print(name_counts)

#highest name count
max_value = None
for row in name_counts:
    count = name_counts[row]
    if max_value is None or count > max_value:
        max_value = count
print("max value is %d") %max_value

top_names = []
for name,count in name_counts.items(): #.items method devide dictionary into key and value
    if count == 22:
        top_names.append(name)
print(top_names)
