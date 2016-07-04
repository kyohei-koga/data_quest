#coding: UTF-8

#extracting unique items set(list)
import csv
f = open("legislators.csv")
legislators = csv.reader(f)
legislators = list(legislators)
gender = []
for row in legislators:
    gender.append(row[3])

gender_unique = set(gender)
print("\n")
print(gender_unique)

party = []
for row in legislators:
    party.append(row[6])

party_unique = set(party)
print(party_unique)


#missing value ex) ''
for gender in legislators:
    if gender[3] == '':
        gender[3] = 'M'

#parsing data
birth_years = []
for row in legislators:
    parts = row[2].split("-")
    birth_years.append(parts[0])

print(birth_years[:5])

#Try/except blocks
#Try/except blocks can deal with error
#Instead of sttoping the code from executing, it will be handled by the "except" statment
try:
    float("hello")
except Exception:
    print("Error converting to float..")

#Excepttion instance
#Exceptino class has certain prperties that allow us to debug the error.
#use as statment,"Exception as exc",and then print out type of exc.
#This means we can print out error message

try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc)) #print out error message

#The pass keyword
#using pass in except statement, we can pass the process happend error and continu next process.

converted_years = []
for year in birth_years:
    try:
        year = int(year)
    except:
        pass
    converted_years.append(year)
print(converted_years[:5])

#convert to integer
for row in legislators:
    birth_years = row[2].split("-")
    try:
        birth_years[0] = int(birth_years[0])
    except:
        birth_years[0] = 0
    row.append(birth_years[0]) #legislators will have extra column, which will be bitrth year.
print(legislators[:3])
