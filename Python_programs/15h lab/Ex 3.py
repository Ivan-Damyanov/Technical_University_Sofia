#Exercise 3
import json
dict={"aaaa":5,"ddd":True,"ccc":[2,3,4],"bbb":3.45}
print(dict)
with open('data.json', 'w') as f: # от структуриран тип в JSON
    json.dump(dict,f)
with open('data.json','r') as f: # от JSON в структурирани данни
    dict=json.load(f)
json_str=json.dumps(dict,indent = 4, sort_keys=True)
print(json_str)
