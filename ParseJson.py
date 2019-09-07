import json

dictionary = '{"k1": "val1", "k2": 11, "k3": "Sridhar"}'
json_result = json.loads(dictionary)
print(json_result)
