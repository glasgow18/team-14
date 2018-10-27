import json
import os


with open("population_data.json", "r") as f:
    data = json.loads("".join(f.read()))
    a = (f.readlines())
    #activity = json.loads("".join(f.readlines()))
for i in data:
    print(i["description"])
#print(len(a))

