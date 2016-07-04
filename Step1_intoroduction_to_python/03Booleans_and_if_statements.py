# coding: UTF -8
f = open("crime_rates.csv")
r = f.read()
crime_sp = r.split("\n")
crime_rates = []
cities = []
for row in crime_sp:
    row_list = row.split(",")
    crime_rates.append(int(row_list[1]))
    cities.append(row_list[0])

print(cities[0:5])
print(crime_rates[0:5])
#If statements
result = 0
if cities[2] == 'Anchorage':
    result = 1
print(result)

#Find the highest crime rate
highest = crime_rates[0]
print("highest=%d") %highest
for rate in crime_rates:
    if highest < rate:
        highest = rate
print("highest=%d") %highest
