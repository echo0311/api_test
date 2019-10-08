# -*- coding: utf-8 -*-
import requests
import json

requests.packages.urllib3.disable_warnings()


class RunMethod:
    def __init__(self, host=None):
        if host is None:
            self.host = 'https://192.168.2.183'
        else:
            self.host = host

    def send_get(self, url, data=None, headers=None):
        res = None
        try:
            if headers is None:
                # res = requests.get(url=url, data=data, verify=False).json()  # verify=False 忽略SSL错误
                res = requests.get(url=url, data=data, verify=False)
            else:
                # res = requests.get(url=url, data=data, headers=headers, verify=False).json()
                res = requests.get(url=url, data=data, headers=headers, verify=False)
            # return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)
            return res
        except (requests.ConnectionError,requests.HTTPError,requests.URLRequired,requests.Timeout,requests.ConnectTimeout) as e:
            print(e)

    def send_post(self,url, data, headers=None):
        res = None
        try:
            if headers is None:
                res = requests.post(url=url, data=data, verify=False)
            else:
                res = requests.post(url=url, data=data, headers=headers, verify=False)
            return res
        except (requests.ConnectionError, requests.HTTPError, requests.URLRequired, requests.Timeout, requests.ConnectTimeout) as e:
            print(e)

    def send_put(self, url, data=None, headers=None):
        res = None
        try:
            if headers is None:
                res = requests.put(url=url, data=data, verify=False)
            else:
                res = requests.put(url=url, data=data, headers=headers, verify=False)
            return res
        except (requests.ConnectionError, requests.HTTPError, requests.URLRequired, requests.Timeout, requests.ConnectTimeout) as e:
            print(e)

    def send_delete(self, url, data=None, headers=None):
        res = None
        try:
            if headers is None:
                res = requests.delete(url=url, data=data, verify=False)  # verify=False 忽略SSL错误
            else:
                res = requests.delete(url=url, data=data, headers=headers, verify=False)
            return res
        except (requests.ConnectionError, requests.HTTPError, requests.URLRequired, requests.Timeout, requests.ConnectTimeout) as e:
            print(e)

    def run_main(self, url, method, data=None, headers=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data, headers)
        elif method == 'POST':
            res = self.send_post(url, data, headers)
        elif method == 'PUT':
            res = self.send_put(url, data, headers)
        else:
            res = self.send_delete(url, data, headers)
        return res


if __name__ == '__main__':
    url = 'https://192.168.0.114/api/overview'
    header = {
        "ESGSESSIONID": "4263947253303185459",
        "auth": "YXV0bzoxNTU3MjMwMDY4MjUyOmZjNjgwM2VmNWM1MGE0ODU3YzQyMjllZDNmMDZlYjkxOkVTQUdF"
    }
    run = RunMethod()
    print(run.run_main(url, 'GET', headers=header))
