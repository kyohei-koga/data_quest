#coding: UTF-8

#Darabase
#As the data gets larger, it becomes more difficult to load the file into a computer's memory, which is how tools like Pandas work with data.
import sqlite3
import csv
import sys
f = open("recent_grads.csv")
reader = csv.reader(f)
recent_grads_list = []
for row in reader:
    recent_grads_list.append(row)
recent_grads_list = recent_grads_list[1:]

con = sqlite3.connect("jobs.db")
cur = con.cursor()
#create table
cur.execute('CREATE TABLE recent_grads(Rank, Major_code, Major, Major_category, Total, Sample_size, Men, Women, ShareWomen, Employed, Full_time, Part_time, Full_time_year_round, Unemployed, Unemployment_rate, Median, P25th, P75th, College_jobs, Non_college_jobs, Low_wage_jobs)')
#Insert a row of date
for row in recent_grads_list:
    table_value = (row[0],
    row[1],row[2],row[3],
    row[4],row[5],row[6],
    row[7],row[8],row[9],
    row[10],row[11],row[12],
    row[13],row[14],row[15],
    row[16],row[17],row[18],
    row[19],row[20],)
    cur.execute("insert into recent_grads values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",table_value)
print(cur.fetchone())

con.commit()
cur.close()
