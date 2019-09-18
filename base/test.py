# -*- coding: utf-8 -*-
import time

vdc_id = '5'
path = '/api/cloud/virtualdatacenters/%s/virtualappliances?startwith=0&limit=30' % int(vdc_id)
print(path)

data = {
    "add_user": {
        "idUserGroup": 1,
        "name": "test",
        "email": "test@123.com",
        "nick": "test",
        "password": "test@",
        "surePassword": "test@",
        "role": "1",
        "resourceApplication": "",
        "active": True,
        "links": [
            {
                "title": "超级管理员",
                "rel": "role",
                "type": "application/vnd.esage.role+json",
                "href": "https://192.168.3.112:443/api/admin/roles/1"
            },
            {
                "title": "privileges",
                "rel": "privileges",
                "type": "application/vnd.esage.privileges+json",
                "href": "https://192.168.3.112:443/api/admin/roles/1/action/privileges"
            },
            {
                "title": "Global scope",
                "rel": "scope",
                "type": "application/vnd.esage.scope+json",
                "href": "https://192.168.3.112:443/api/admin/scopes/1"
            }
        ],
        "surname": "默认分组",
        "locale": "en_US"
    }
}
print(type(data))
num = str(int(time.time()))
data['add_user']['name'] += num
data['add_user']['nick'] += num
print(data)
