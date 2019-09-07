import requests

# Adding customized headers
headersData = {
    "Key1": 'First key value',
    "Key2": 'Second key value',
    "Key3": 'Third key value'
}
response = requests.get("http://httpbin.org/get", headers=headersData)
print(response.text)
