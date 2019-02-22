# coding:utf-8
import requests
import json
import ast
import time
class Request():

    def __init__(self, url, method, headers, params, status_code, code):
        self.url = str(url)
        self.method = str(method)
        self.headers = str(headers)
        self.params = str(params)
        self.status_code = int(status_code)
        self.code = str(code)
        
        # 测试传递的参数
        # print("Request.py测试传递的参数:", self.url, self.method,self.headers, self.params, self.status_code, self.code)

    def getRespon(self):
        # 请求方式
        try:
            if self.method == "get":
                if self.params == "null":
                    response = requests.get(self.url, headers=ast.literal_eval(self.headers))
                else:
                    response = requests.get(self.url, params=ast.literal_eval(self.params), headers=(ast.literal_eval(self.headers)))
            elif self.method == "post":
                if self.params == "null":
                    response = requests.post(self.url, headers=ast.literal_eval(self.headers))
                else:
                    response = requests.post(self.url, data=ast.literal_eval(self.params), headers=ast.literal_eval(self.headers))
            response.encoding="utf-8"  # 设置响应数据的编码
            return response
        except Exception as e:
            print(now, 'Request 请求失败:', e,'---',self.url, self.method, self.params)
            return e

    def getJson(self):
        # 以Json格式响应的数据
        try:
            json_data = self.getRespon().json()
            return json_data
        except Exception as e:
            print(now, 'Request 响应失败:', e,'---',self.url, self.method, self.params)
            return 'Request End'

if __name__ == '__main__':

    now = time.strftime("[%Y-%m-%d %H:%M:%S]")
    # 测试请求数据
    re1 = Request(
        'http://www.kuaidi100.com/query',
        'get1',
        {"Content-Type": "application/json"},
        {"type":"huitongkuaidi","postid":"350757819118"},
        200,
        0) 
    re2 = Request(
        'http://www.weather.com.cn/data/sk/101190408.html',
        'get',
        {"Content-Type": "text/html"},
        "null", 
        200,
        0)
    re3 = Request(
        'https://www.v2ex.com/api/nodes/show.json',
        'get',
        {"Content-Type": "text/html"},
        {'name': 'java'},
        200,
        0
    )
    print(re1.getJson())
    print(re2.getJson())
    print(re3.getJson())

    

    

    




