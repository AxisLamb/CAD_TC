#coding=utf-8
import types
import requests


class HttpUtil:

    # post url + json
    def postWithAuth(self, url, Authorization, json):
        try:
            headers = {'Content-Type': 'application/json; charset=utf-8',
                       'Authorization': Authorization}
            res = requests.post(url, json=json, headers=headers)
            return res.json()
        except BaseException as e:
            print(e)

    def post(self, url, json):
        try:
            headers = {'Content-Type': 'application/json; charset=utf-8'}
            res = requests.post(url, json=json, headers=headers)
            return res.json()
        except BaseException as e:
            print(e)

    # post url + json
    def postWithFun(self, url, json, fun):
        try:
            headers = {'Content-Type': 'application/json; charset=utf-8'}
            res = requests.post(url, json=json, headers=headers)
            return res.json()
        except BaseException as e:
            print(e)
            # 回调函数 回滚用
            if isinstance(fun, types.FunctionType):
                fun()

http_util = HttpUtil()

