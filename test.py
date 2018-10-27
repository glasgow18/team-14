import json
import os


with open("test.json", "r", encoding='utf-8') as f:
    data = json.loads("".join(f.read()))
    a = (f.readlines())
    #activity = json.loads("".join(f.readlines()))
for i in data:
    print(i["description"])
#print(len(a))
