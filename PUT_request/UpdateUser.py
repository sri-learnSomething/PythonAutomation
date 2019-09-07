import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

# Reading input from json file
file = open('C:\\Users\\SridharRaju\\PycharmProjects\\JSONWork\\PUT_request\\UpdateUser.json', 'r')
json_file = file.read()

# Parsing the data in to json format
request_json = json.loads(json_file)
print(request_json)

# make PUT request with input body
response = requests.put(url, request_json)
print(response.status_code)

# Validating the response code
assert response.status_code == 200, "Something went wrong"

# # GET the user details
# response_get = requests.get(url)
# print(response_get)

json_response = json.loads(response.text)
print(json_response)
updatedName = jsonpath.jsonpath(json_response, 'name')
updatedJob = jsonpath.jsonpath(json_response, 'job')
updatedAtList = jsonpath.jsonpath(json_response, 'updatedAt')

print("updated Name: " + str(updatedName[0]))
print("updated Job: " + str(updatedJob[0]))
print("UpdatedAT: " + str(updatedAtList[0]))

# # Fetch HEADER from response
# print(response.headers)
# print(response.headers.get('Content-Length'))
#
# # Parse response to json format
# response_json = json.loads(response.text)
# print(response_json)
#
# # Pick 'id' using Jsonpath
# id = jsonpath.jsonpath(response_json, 'id')
# print(id[0])