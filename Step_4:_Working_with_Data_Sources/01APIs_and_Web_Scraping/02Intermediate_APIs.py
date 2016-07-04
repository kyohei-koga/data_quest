#coding: UTF-8
import requests
#API Authentication
#Most Api requires Authentication
#Create a dictionary of headers, with our Authorization header.
headers = {"Authorization":"token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}

#Make a GET request to the Github API with out headers
#This API endpoint will give us details about Vik Paruchuri.
response = requests.get("https://api.github.com/users/VikParuchuri",headers=headers)

#print the content of the response. As you can see, this token is associated with the account of Vik Paruchuri
print(response.json())
print(response.headers["Content-Type"])
response = requests.get("https://api.github.com/users/VikParuchuri/orgs",headers=headers)
orgs = response.json()

#Endpoints And Objects
#We could also retrive information about other Github users using the same endpoint.
responses = requests.get("https://api.github.com/users/torvalds",headers=headers)
torvalds = responses.json()
responses = requests.get("https://api.github.com/repos/octocat/Hello-World",headers=headers)
hello_workd = responses.json()

#Pagination
#if a user has 1000+ repositories, requesting all of them might take 10+ seconds. This isn't a great user experience,
#so it's typical for API providers to implement pagination.
#This means that the API provider will only return a certain number of records per page.
#You can specify the page number that you want to access. To access all of the pages, you'll need to write a loop.

#We can add two pagination query parameters to it, page, and per_page. page is the page that we want to access,
#and per_page is the number of records we want to see on each page.

params = {"per_page": 30, "page":1}
response = requests.get("https://api.github.com/users/VikParuchuri/starred",headers=headers,params=params)
page1_repos = response.json()

#PUT/PATCH requests
