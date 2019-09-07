import pytest
import requests
import json
import jsonpath


def test_addStudentData():
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\Users\\SridharRaju\\Desktop\\API_tasks\\add_requestJsonBody.txt", "r")
    json_request = json.loads(file.read())
    json_response = requests.post(api_url, json_request)
    print('===== Adding student details in to system =====')
    print(json_response.text)


def test_updateStudentData():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/144321"
    file = open("C:\\Users\\SridharRaju\\Desktop\\API_tasks\\update_requestJsonBody.txt", "r")
    json_request = json.loads(file.read())
    json_response = requests.put(api_url, json_request)
    print('=====Updating student details in to system=====')
    print(json_response.text)


def test_deleteStudentDetails():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/144321"
    json_response = requests.delete(api_url)
    print("=====Deleting student details in to system=====")
    print(json_response.text)


def test_getStudentDetails():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/144321"
    json_response = requests.get(api_url)
    print("===== Displaying Student details =====")
    print(json_response.text)
    # json_response_format = json.loads(json_response.text)
    # print(json_response_format)
    json_response_format = json_response.json()
    studentId = jsonpath.jsonpath(json_response_format, 'data.id')
    assert id[0] == 144321, "Student is not Found in the system"
    # print(studentId)