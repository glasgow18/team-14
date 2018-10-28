import json
import os

# this is just a test file for populating
# can be used for future debugging purposes!

with open("population_data.json", "r") as f:
    data = json.loads("".join(f.read()))
    a = (f.readlines())
    #activity = json.loads("".join(f.readlines()))
for i in data:
    print(i["description"])
