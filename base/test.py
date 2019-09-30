# -*- coding: utf-8 -*-

import requests

url = 'https://192.168.2.180/api/admin/enterprises/1/users/56'

# payload = "{\n    \"idUserGroup\": 1,\n    \"name\": \"test1\",\n    \"email\": \"test@123.com\",\n    \"nick\": \"test1\",\n    \"password\": \"test@123\",\n    \"surePassword\": \"test@123\",\n    \"role\": \"1\",\n    \"resourceApplication\": \"\",\n    \"active\": true,\n    \"links\": [\n        {\n            \"title\": \"超级管理员\",\n            \"rel\": \"role\",\n            \"type\": \"application/vnd.esage.role+json\",\n            \"href\": \"https://192.168.3.112:443/api/admin/roles/1\"\n        },\n        {\n            \"title\": \"privileges\",\n            \"rel\": \"privileges\",\n            \"type\": \"application/vnd.esage.privileges+json\",\n            \"href\": \"https://192.168.3.112:443/api/admin/roles/1/action/privileges\"\n        },\n        {\n            \"title\": \"Global scope\",\n            \"rel\": \"scope\",\n            \"type\": \"application/vnd.esage.scope+json\",\n            \"href\": \"https://192.168.3.112:443/api/admin/scopes/1\"\n        }\n    ],\n    \"surname\": \"默认分组\",\n    \"locale\": \"en_US\"\n}"
headers = {
    'Cookie': "ESGSESSIONID=6750498760856075399;auth=YXV0bzoxNTY5ODI5NTczMTYwOjg1YWU3MWNjOThjMzIwMjY1MjM4N2ZhZmM4MzMyZWMwOkVTQUdF",
    'Accept': "application/vnd.esage.user+json;version=3.0",
}

response = requests.delete(url, headers=headers, verify=False)

print(response.status_code)
