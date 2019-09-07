import pytest
import requests
import json
import jsonpath

base_url = "http://thetestingworldapi.com"


def test_oAuthentication():
    token_url = "http://thetestingworldapi.com/Token"
    data = {
        'grant_type': 'password',
        'username': 'admin',
        'password': 'adminpass'
    }

    response = requests.post(token_url, data)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')

    auth = {
        'Authorization': 'Bearer ' + token_value[0]
    }

    app_url = base_url + "/api/StDetails/144344"
    response = requests.get(app_url, headers=auth)
    print(response)
    print(response.text)
