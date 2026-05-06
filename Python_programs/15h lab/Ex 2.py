#Exercise 2
import json
dict={"aaaa":5,"ddd":True,"ccc":[2,3,4],"bbb":3.45}
print(dict)
json_str=json.dumps(dict, indent = 4, sort_keys=True)
print(json_str)
