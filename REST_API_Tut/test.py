import requests
# allows us to make POST, GET, PUT ect

# Set base url
BASE = "http://127.0.0.1:5000/"

"""response = requests.get(BASE + "helloworld")"""
response = requests.post(BASE + "helloworld")

# print in json format
print(response.json())