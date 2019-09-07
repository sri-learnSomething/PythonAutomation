"""
    Testing aAuthentication
    token_url => "http://thetestingworldapi.com/Token"

- Send request and generate authentication token
- Get this token and store in variable
- Pass this token as a header in other requests
"""

import pytest
import requests
import json
import jsonpath

base_url = "http://thetestingworldapi.com"


def test_oAuthentication():
    token_url = "http://thetestingworldapi.com/Token"
    data = {
        "grant_type": "password",
        "username": "admin",
        "password": "adminpass"
    }

    response = requests.post(token_url, data)
    #print(response.text)
    token_value = jsonpath.jsonpath(response.json(), "access_token")
    print(token_value)

    my_auth = {
        'Authorization': 'Bearer ' + token_value[0]
    }
    print(my_auth['Authorization'])

    app_url = base_url + "/api/StDetails/144343"
    response = requests.get(app_url, headers=my_auth)
    print(response.text)
