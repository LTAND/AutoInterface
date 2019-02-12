# coding:utf-8
import requests
import json
import ExcelUtil as readSheet
import ast

class RequUtil():

    def __init__(self, url, method, headers, params, status_code, code):
        self.url = str(url)
        self.method = str(method)
        self.headers = str(headers)
        self.params = str(params)
        self.status_code = int(status_code)
        self.code = int(code)
        
        # 测试传递的参数
        print("测试传递的参数:",self.url, self.method, self.headers, self.params, self.status_code, self.code)

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
        except:
            print('请求失败!')

    def getJson(self):
        # 以Json格式响应的数据
        # try:
        #     json_data = self.getRespon().json()
        #     return json_data
        # except:
        #     print('无法获取响应数据!')
        json_data = self.getRespon().json()
        return json_data

if __name__ == '__main__':

    # 读取Excel数据
    filepath = r"D:\vsworkspace\20181022自动化接口3\02.xls"    # Excel文件路径
    sheetName = "Sheet1"        # 表名
    sheet = readSheet.ExcelUtil(filepath, sheetName)
    sheet_data = sheet.dict_data()
    
    # 测试请求数据
    re1 = RequUtil(
        'http://www.kuaidi100.com/query',
        'get',
        {"Content-Type": "application/json"},
        {"type":"huitongkuaidi","postid":"350757819118"},
        200,
        0) 
    re2 = RequUtil(
        'http://www.weather.com.cn/data/sk/101190408.html',
        'get',
        {"Content-Type": "text/html"},
        "null", 
        200,
        0)
    print(re1.getJson())
    print(re2.getJson())

    

    

    




