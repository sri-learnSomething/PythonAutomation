import requests
import json
import jsonpath
import pytest


@pytest.mark.Smoke
def test_fetch_userData():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    json_response = json.loads(response.text)
    # print(json_response)
    for i in range(0, 3):
        jsonData = jsonpath.jsonpath(json_response, f'data[{i}].first_name')
        print(jsonData[0])
