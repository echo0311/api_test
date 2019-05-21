# -*- coding: utf-8 -*-
import mock
import json
from base import api_requests


def mock_test(mock_method, url, method, response_data, request_data=None):
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url, method, request_data)
    return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    url = 'http://www.wanandroid.com/banner/json'
    response_data = {
        "desc": "",
        "id": 4,
        "imagePath": "http://www.wanandroid.com/blogimgs/ab17e8f9-6b79-450b-8079-0f2287eb6f0f.png",
        "isVisible": 1,
        "order": 0,
        "title": "看看别人的面经，搞定面试~",
        "type": 1,
        "url": "http://www.wanandroid.com/article/list/0?cid=73"
    }
    run = api_requests.RunMain
    res = mock_test(run.run_main, url, 'GET',response_data)
    print(res)
