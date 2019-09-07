import requests
import pytest
import json
from requests.auth import HTTPBasicAuth

req_url = "https://github.com/"

def test_with_authentication():
    response = requests.get(req_url, auth=HTTPBasicAuth('rajusridhar.1975@gmail.com', 'xxxxx'))
    print()
    print(response.text)