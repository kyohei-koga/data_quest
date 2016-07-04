#coding: UTF-8

#APIs are used to dynamically query and retrieve data.
#In order to get the data, we make a request to the webserver that we want to get data from. The server then replies with our data. In Python, we use the requests library to do this.
#requests library: http://www.python-requests.org/en/latest/

#type of request
#The most commonly used one, a GET request, is used to retrieve data.
#Make a get request to get the latest position of the international space station from the opennotify api.
import requests
response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code
print(status_code)
print(response.content)

#Status codes indicate information about what happened with a request.

#    200 -- everything went okay, and the result has been returned (if any)
#    301 -- the server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
#    401 -- the server thinks you're not authenticated. This happens when you don't send the right credentials to access an API (we'll talk about this in a later mission).
#    400 -- the server thinks you made a bad request. This can happen when you don't send along the right data, among other things.
#    403 -- the resource you're trying to access is forbidden -- you don't have the right permissions to see it.
#    404 -- the resource you tried to access wasn't found on the server.

# Enter your answer below.
response = requests.get("http://api.open-notify.org/iss-pass")
status_code = response.status_code
print(status_code)

#Query parameters
#set up the parameters we want to pass the API
#This is the latitude and longitude of New York City.
parameters = {"lat":40.71,"lon":-74}

#Make a get request with the parameters
response = requests.get("http://api.open-notify.org/iss-pass.json",params=parameters)

#print the content of the response(the data the server returned)
print(response.content)

#This gets the same data as the command above
#response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
#print(response.content)

#Jason Format
#The jason library has two main method
#    dumps -- Takes in a Python object, and converts it to a string.
#    loads -- Takes a json string, and converts it to a Python object.

#example code
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains))

#Import the json library
import json

#Use json.dumps to convert best_food_chains to a string
best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string))

#Convert best_food_chains_string back into a list
print(type(json.loads(best_food_chains_string)))

#Getting json from a request
data = response.json()
print(type(data))
print(data)

first_pass_duration = data["response"][1]["duration"]
print(first_pass_duration)

#contetype
#content-type is the most important key for now.
#It tells us the format of the response, and how to decode it.

print(response.headers) #response headers have metadata containing information on how the data was generated and how to decode it.It will be shown as dictionary.
content_type = response.headers['content-type']
print(content_type)
