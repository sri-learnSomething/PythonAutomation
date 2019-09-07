import requests

param = {'name': 'testingworld', 'email': 'testing@test.com', 'number': '+91 1234 567890'}
response = requests.get("http://httpbin.org/get", params=param)
print(response.text)