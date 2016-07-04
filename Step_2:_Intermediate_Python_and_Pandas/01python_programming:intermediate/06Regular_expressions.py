#coding: UTF-8

#Reading and printing dataset
import csv
f = open("askreddit_2015.csv","r")
csv_reader = csv.reader(f)
posts_with_header = list(csv_reader)
posts = posts_with_header[1:]
#for post in posts[:10]:
#    print(post)

#re module
#with re.search(regex, string), we can check if string is a match for regex.
import re

of_reddit_count = 0
for post in posts:
    if re.search("of Reddit",post[0]) != None:
        of_reddit_count += 1
print(of_reddit_count)

#improve above statment

of_reddit_count = 0
for post in posts:
    if re.search("of [Rr]eddit",post[0]) != None: #search "Reddit" and "reddit" case.
        of_reddit_count += 1
print(of_reddit_count)

#Escaping special characters
serious_count = 0
for post in posts:
    if re.search("\[Serious\]",post[0]) != None: #\(backslash) to escape characters regular expression.
        serious_count += 1
print(serious_count)

#More inconsistency
serious_count = 0
for post in posts:
    if re.search("[\[\(][Ss]erious[\]\)]", post[0]) != None:
        serious_count += 1
print(serious_count)

#substituting strings
posts_new = []
for post in posts:
    post[0] = re.sub("[\[\(][Ss]erious[\]\)]","[Serious]",post[0]) #sub() is substitute function.
    posts_new.append(post)

strings = ['War of 1812', 'There are 5280 feet to a mile', 'Happy New Year 2016!']
year_strings = []
for string in strings:
    if re.search("[1-2][0-9]{3}",string) != None: #4の位1 or 2、3〜1の位0〜9
        year_strings.append(string)
