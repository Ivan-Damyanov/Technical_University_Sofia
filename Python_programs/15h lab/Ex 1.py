#Exercise 1

import json
json_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]} '
data = json.loads(json_string)
print("JSON данни:")
print(data)
print("Поле Име:")
print(data['name'])
