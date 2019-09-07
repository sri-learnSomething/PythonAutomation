import pytest
import json
import jsonpath
import requests

base_url = "http://thetestingworldapi.com"


def test_addNewStudent():
    global id
    req_url = base_url + "/api/studentsDetails"
    file = open("C:\\Users\\SridharRaju\\Desktop\\API_tasks\\add_requestJsonBody.txt", "r")
    json_request = json.loads(file.read())
    response = requests.post(req_url, json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])


def test_getStudentDetails():
    req_url = base_url + "/api/studentsDetails/" + str(id[0])
    response = requests.get(req_url)
    print(response)