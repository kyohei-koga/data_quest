#coding: UTF-8
#math module
import math
a = math.sqrt(16.0)
b = math.ceil(111.3) #ceil function returns the smallest integer that is greater than or equal to the input.
c = math.floor(89.9) # floor function returns the largest integer less or equal to the input
print a,b,c

#Variables within modules
print("\npi=%s") %math.pi

#csv module
import csv
f = open("nfl.csv","r")
csvreader = csv.reader(f)
nfl = list(csvreader)
print(nfl[0:2])

#counting how many times a team won
import csv
f = open("nfl.csv","r")
csvreader = csv.reader(f)
nfl = list(csvreader)
patriots_wins = 0
for winer in nfl:
    if winer[4] == "New England Patriots":
        patriots_wins += 1
print(patriots_wins)

#Making a function to count wins
def nfl_wins(team_name):
    win_count = 0
    for winer in nfl:
        if winer[4] == team_name:
            win_count += 1
    return win_count
print("number of wins by the Dallas Cowboys is %d" %nfl_wins("Dallas Cowboys"))
print("\nnumber of wins by the Atlanta Falcons is %d" %nfl_wins("Atlanta Falcons"))
