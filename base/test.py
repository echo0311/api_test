# -*- coding: utf-8 -*-

import requests

vdc_id = '5'
path = '/api/cloud/virtualdatacenters/%s/virtualappliances?startwith=0&limit=30' % int(vdc_id)
print(path)



url = "https://192.168.3.180/api/admin/enterprises/1/users"

payload = "{\n    \"idUserGroup\": 1,\n    \"name\": \"test1\",\n    \"email\": \"test@123.com\",\n    \"nick\": \"test1\",\n    \"password\": \"test@123\",\n    \"surePassword\": \"test@123\",\n    \"role\": \"1\",\n    \"resourceApplication\": \"\",\n    \"active\": true,\n    \"links\": [\n        {\n            \"title\": \"超级管理员\",\n            \"rel\": \"role\",\n            \"type\": \"application/vnd.esage.role+json\",\n            \"href\": \"https://192.168.3.112:443/api/admin/roles/1\"\n        },\n        {\n            \"title\": \"privileges\",\n            \"rel\": \"privileges\",\n            \"type\": \"application/vnd.esage.privileges+json\",\n            \"href\": \"https://192.168.3.112:443/api/admin/roles/1/action/privileges\"\n        },\n        {\n            \"title\": \"Global scope\",\n            \"rel\": \"scope\",\n            \"type\": \"application/vnd.esage.scope+json\",\n            \"href\": \"https://192.168.3.112:443/api/admin/scopes/1\"\n        }\n    ],\n    \"surname\": \"默认分组\",\n    \"locale\": \"en_US\"\n}"
headers = {
    'Cookie': "ESGSESSIONID=5113480537785423510; auth=YXV0bzoxNTY5NDg5NTA3MjQ4OmQwZTc2Nzg4OTY0ODM5NDQ5YzAyM2VlN2YwMzVhNGNlOkVTQUdF",
    'Content-Type': "application/json",
    'Accept': "application/vnd.esage.user+json;version=3.0",
    'cache-control': "no-cache",
    'Postman-Token': "086b51f7-64ab-4bc7-a328-23371b1f7cb7"
    }


response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
