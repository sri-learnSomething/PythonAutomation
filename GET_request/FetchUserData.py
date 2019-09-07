import requests
import json
import jsonpath

"""
    Using the base url : https://reqres.in/
    relative url : https://reqres.in/api/users?page=2
"""

url = "https://reqres.in/api/users?page=2"

# sending a GET request
response = requests.get(url)

# Parse response to Json format
json_response = json.loads(response.text)
print(json_response)

# Fetch value using json path
noOfPages = jsonpath.jsonpath(json_response, 'total_pages')

for i in range(0, 3):
    jsonData = jsonpath.jsonpath(json_response, f'data[{i}].first_name')
    print(jsonData[0])