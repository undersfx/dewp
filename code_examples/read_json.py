import json


with open('data.json', 'r') as file:
    data = json.load(file)
    print(data['records'][0])
    print(data['records'][0]['name'])