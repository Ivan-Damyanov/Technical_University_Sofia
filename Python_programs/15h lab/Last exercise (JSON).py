#Last exercise
#dict[key] = int_value
import json

dict={}
for i in range(0, 5):
    key = input("Key for dict: ")
    while True:
        try:
            value = int(input("Value of that key: "))
            break
        except ValueError:
            print("Must be int!!!")
    dict[key] = value

with open('last_exercise_data.json', 'w') as f:
    json.dump(dict,f)
with open('last_exercise_data.json','r') as f:
    dict=json.load(f)
json_str=json.dumps(dict,indent = 4, sort_keys=True)
print(json_str)
