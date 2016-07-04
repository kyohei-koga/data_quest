#coding UTF-8

#Introduction
#As we learn about web scraping, we'll be heavily using the requests library, which enables us to download a webpage, and the beautifulsoup library,
#which enables us to extract the relevant parts of a webpage.

#Webpage Structure
#Webpages are coded in HyperText Markup Language (HTML).
#https://developer.mozilla.org/en-US/Learn/Getting_started_with_the_web/HTML_basics

import requests
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
content = response.content

#Retrieving elements From A page
#In order to parse the webpage with python, we'll use the BeautifulSoup library. This library allows us to extract tags from an HTML document.
#https://www.crummy.com/software/BeautifulSoup/

from bs4 import BeautifulSoup
#Initialize the parser, and pass in the content we grabbe earlier
#HTML documents can be thought of as trees due to how tags are nested, and BeautifulSoup works the same way.
parser = BeautifulSoup(content, 'html.parser')
#Get the body tag from the document.
#Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
#With BeautifulSoup, we can access beanches by simple using tag types as
body = parser.body

#Get the p tag from the body
p = body.p

#print the text of the p tag
#Text is a property that gets the inside text fo a tag.
print(p.text)
head = parser.head
title = parser.title
title_text = title.text
print(title_text)

#Using Find All
#While it's nice to use the tag type as a property, it doesn't always lead to a very robust way to parse a document.
#Usually, it's better to be more explicit and use the find_all method.
#find_all will find all occurences of a tag in the current element.

parser = BeautifulSoup(content,'html.parser')
#Get a list of all occurences of the body tag in the element.
body = parser.find_all('body')

#Get the paragraph tag
p = body[0].find_all("p")

#get the text
print(p[0].text)

head = parser.find_all("head")
title = head[0].find_all("title")
title_text = title[0].text
print(title_text)

#Element ids
#HTML allows elements to have ids. These ids are unique, and can be used to refer to a specific element.
#The div tag is used to indicate a division of the page -- it's used to split up the page into logical units.
#Luckily, the paragraphs have been assigned ids -- we can easily access them, even through they're nested.

#Get the page content and setup a new parser
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
content = response.content
parser = BeautifulSoup(content,"html.parser")

#Pass in the id attribute to only get elements with a certain id.
first_paragraph = parser.find_all("p", id="first")[0]
print(first_paragraph.text)
second_paragraph = parser.find_all("p", id="second")[0]
print(second_paragraph.text)

#Element classes
#HTML also enables elements to have classes. Classes aren't globally unique, and usually indicate that elements are linked.
#Get the website that contains classes
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
content = response.content
parser = BeautifulSoup(content,'html.parser')

#Get the first innner paragraph.
#Find all the paragraph tags with the class inner-text.
#Then take the first element in that list
first_inner_paragraph = parser.find_all("p",class_="inner-text")[0]
print(first_inner_paragraph.text)
second_iner_paragraphs = parser.find_all("p",class_="inner-text")[0].text
first_outer_paragraph_text = parser.find_all("p",class_="outer-text")[0].text
print(first_outer_paragraph_text)


#CSS Selectors
#Cascading Style Sheets, or CSS, is a way to add style to HTML pages.
#https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Getting_started
#This CSS will make all the text in any paragraphs with the class inner-text red.

#Using CSS Selectors
#With BeautifulSoup, we can use CSS selectors very easily. We just use the .select method.

# Get the website that contains classes and ids
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all the elements with the first-item class
first_items = parser.select(".first-item")

# Print the text of the first paragraph (first element with the first-item class)
print(first_items[0].text)
outer_text = parser.select(".outer-text")
first_outer_text = outer_text[0].text

second = parser.select("#second")
second_text = second[0].text

#Using Nested CSS Selectors
#Just like how HTML has nested tags, we can also nest CSS Selectors to select items that are nested.
#So we could use CSS selectors to find all of the paragraphs inside the body tag, for instance.

#Get the super bowl box score data
response = requests.get("http://dataquestio.github.io/web-scraping-pages/2014_super_bowl.html")
content = response.content
parser = BeautifulSoup(content,"html.parser")

#Find the number of turnobers committed bo the seahawks
turnovers = parser.select("#turnovers")[0]
seahawks_turnovers = turnovers.select("td")[1]
seahawks_turnovers_count = seahawks_turnovers.text
print(seahawks_turnovers_count)

patriots_total_plays_count = parser.select("#total-plays")[0].select("td")[2].text
seahawks_total_yards_count = parser.select("#total-yards")[0].select("td")[1].text
