#coading: UTF-8

#Introduction to the data
import csv
f = open("nfl_suspensions_data.csv","rU") #read mord rU
nfl_suspensions =  list(csv.reader(f))
nfl_suspensions = nfl_suspensions[1:]

years_column = nfl_suspensions[5]
years = {}

for suspension in nfl_suspensions:
    row_year = suspension[5]
    if row_year in years:
        years[row_year] = years[row_year] + 1
    else:
        years[row_year] = 1

print(years)
#Unique values
teams = [row[1] for row in nfl_suspensions] #extract the column want
unique_teams = set(teams)
print(unique_teams)

games = [row[2] for row in nfl_suspensions]
unique_games = set(games)
print(unique_games)

#Suspension class
class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[3]

third_suspension = Suspension(nfl_suspensions[2])

#Tweaking the Suspension class
class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[3])
        except:
            self.year = 0

    def get_year(self):
        return self.year

missing_year = Suspension(nfl_suspensions[23])
zero = missing_year.get_year()
