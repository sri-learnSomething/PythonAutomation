import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users"


@pytest.fixture(scope="module")
def start_execution():
    global file
    file = open('C:\\Users\\SridharRaju\\PycharmProjects\\JSONWork\\POST_request\\CreateUsers.json', 'r')


@pytest.mark.Smoke
def test_create_new_user(start_execution):
    json_file = file.read()
    request_json = json.loads(json_file)
    print(request_json)

    # make POST request with input body
    response = requests.post(url, request_json)
    print(response)

    # Validating the response code
    assert response.status_code == 201, "Something went wrong"

    # Fetch HEADER from response
    print(response.headers)
    print(response.headers.get('Content-Length'))

    # Parse response to json format
    response_json = json.loads(response.text)
    print(response_json)

    # Pick 'id' using Jsonpath
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])


@pytest.mark.Sanity
def test_create_other_user(start_execution):
    file = open('C:\\Users\\SridharRaju\\PycharmProjects\\JSONWork\\POST_request\\CreateUsers.json', 'r')
    json_file = file.read()
    request_json = json.loads(json_file)
    print(request_json)
    response = requests.post(url, request_json)
    print(response)
    print(response.headers)
    print(response.headers.get('Content-Length'))
    response_json = json.loads(response.text)
    print(response_json)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])
