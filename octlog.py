#!/usr/bin/env python3
import json
import requests
endpoint = '/api/files'

myHeader = {
    'content-type': 'Application/json',
    'X-Api-Key': ''
}

r = requests.get('http://192.168.1.4'+endpoint, headers=myHeader)
#print(r.text)

myDict = json.loads(r.text)

print(myDict['files'][0]['name'])
print(myDict['files'][0])

for file in myDict['files']:
    print(file['name'])
