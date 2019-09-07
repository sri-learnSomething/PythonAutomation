import requests
import pytest
import json
import jsonpath

base_url = "http://thetestingworldapi.com"


def test_Add_new_data():
    app_url = base_url + "/api/studentsDetails"
    print("\nAdding new student url : " + app_url)
    file = open("C:\\Users\\SridharRaju\\Desktop\\API_tasks\\add_requestJsonBody.txt", "r")
    json_request = json.loads(file.read())
    response = requests.post(app_url, json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_url = base_url + "/api/technicalskills"
    print("Technical details url: " + tech_url)
    file = open("C:\\Users\\SridharRaju\\Desktop\\API_tasks\\tech_detailsJson.txt", "r")
    json_request = json.loads(file.read())
    print(json_request)
    json_request['id'] = int(id[0])
    json_request['st_id'] = id[0]
    response = requests.post(tech_url, json_request)
    print(response.status_code)
    print(response.text)

    add_url = base_url + "/api/addresses"
    print("Requested url : " + add_url)
    file = open("C:\\Users\\SridharRaju\\Desktop\\API_tasks\\add_address.txt", "r")
    json_request = json.loads(file.read())
    print(id[0])
    json_request['stId'] = str(id[0])
    print(json_request['stId'])
    response = requests.post(add_url, json_request)
    print(response.status_code)
    print(response.text)

    final_url = base_url + "/api/FinalStudentDetails/" + str(id[0])
    print("Requested url: " + final_url)
    json_response = requests.get(final_url)
    print(json_response.status_code)
    print(json_response.text)
