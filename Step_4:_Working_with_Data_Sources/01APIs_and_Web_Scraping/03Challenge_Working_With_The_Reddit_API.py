#coding: UTF-8
import requests
#In this challenge, you'll practice the following:
#   Getting a list of trending article in a subreddit
#   Exploring the comments of a single article
#   Posting our own comment on the article

#Authenticating with the API

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"} #Authentication
params = {"t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)

python_top = response.json()
#Getting the most upvoted article
#The variable python_top is a dictionary that contains information about all of the individual articles submitted in the past day.

python_top_articles = python_top["data"]["children"]
most_upvoted = ""
most_upvotes = 0
for article in python_top_articles:
    ar = article["data"]
    if ar["ups"] >= most_upvotes:
        most_upvoted = ar["id"]
        most_upvotes = ar["ups"]

#Getting article comments
