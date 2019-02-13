# -*- coding:utf-8 -*-
import time
import unittest
import HTMLTestReportCN

import ExcelUtil as readSheet
import RequUtil as request
import time
import ast
import json

def make_response():

    # 传递Excel数据请求参数
    def make_dict(curRow, sp):
        # 将参数根据划分转化字典
        curList = curRow.split(sp)
        keys.append(str(curList[0]))
        values.append(str(curList[1]))
        return dict(zip(keys, values))

    for i in range(0, len(sheet_data)):
        keys = []      # 存放参数名 eg：type
        values = []    # 存放参数值 eg：huitongkuaidi
        ParamsNum = int(sheet_data[i]['Params'])  # 每行的参数个数   eg：2

        # 参数类别处理
        if ParamsNum == 0:
            Params.append("null")
        elif ParamsNum >= 1:
            for x in range(1, ParamsNum+1):
                curDict = make_dict(sheet_data[i]['Parameter'+str(x)], "=")
            Params.append(curDict)
        elif ParamsNum == -1:
            Params.append(sheet_data[i]['Parameter1'])

        # 传参请求
        reps.append(request.RequUtil(
            sheet_data[i]['Url'],
            sheet_data[i]['Method'],
            sheet_data[i]['Headers'],
            Params[i],
            sheet_data[i]['Status_code'],
            sheet_data[i]['Code']
        ))

        # 测试每条请求响应数据
        # print('响应的数据:',reps[i].getJson())
 
# 测试用例
class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self): 
        pass

    def testCase1(self):
        self.assertEqual(2,2,"testError")

class test_sheet1(unittest.TestCase):
    # 设计测试用例模板
    def test_1_2_3(self):
        for i in range(0, len(reps)):
            try:
                # if reps[i].getJson()['status'] == 200:
                # reps[i].getJson()['status'] == 200 # 断言判断请求状态
                print("\n========================================"+now+"=============================================")
                print("用例编号:", sheet_data[i]['Id'], "\n用例名称:", sheet_data[i]['Name'], '\n请求地址:',sheet_data[i]['Url'], '\n请求状态:',reps[i].getJson()['status'], '\n请求参数:', Params[i])
                print('响应数据:\n',json.dumps(reps[i].getJson(), sort_keys=False, indent=4, ensure_ascii=False))
            except:
                print(sheet_data[i]['Id'],sheet_data[i]['Name'],'请求出错!!!')
     
#添加Suite
def Suite():
    #定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    #将测试用例加入到容器
    suiteTest.addTest(MyTestCase("testCase1"))
    suiteTest.addTest(test_sheet1("test_1_2_3"))
    return suiteTest

# 创建html报告
class HtmlReport():
    def __init__(self, fp, title, description, tester):
        self.fp = fp
        self.title = title
        self.description = description
        self.tester = tester

    def createdHtml(self):
        #生成报告的Title,描述
        runner = HTMLTestReportCN.HTMLTestRunner(
            stream=self.fp,
            title=self.title,
            description=self.description,
            tester=self.tester
        )
        return runner

if __name__ == '__main__':
    # 读取Excel数据
    filepath = r"D:\vsworkspace\2018年10月\AutoInterface\20181022自动化接口v1.3\dataExcel\02.xls"    # Excel文件路径
    sheetName = "Sheet1"        # 表名
    sheet = readSheet.ExcelUtil(filepath, sheetName)
    sheet_data = sheet.dict_data()

    reps = []   # 存放表格每一行请求对象
    Params = []  # 存放每一行的请求参数

    make_response()  # 完成响应数据赋值

    # 生成报告信息配置
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    htmlPath = 'D:\\vsworkspace\\2018年10月\AutoInterface\\20181022自动化接口v1.3\\reportHtml\\'+now+'_report.html'
    fp = open(htmlPath, 'wb')
    title = '自动化测试报告'
    description = '详细测试用例结果'
    tester = 'Tan'
    
    # 运行测试用例
    htmlObj = HtmlReport(fp, title, description, tester)
    htmlObj.createdHtml().run(Suite())
    # 关闭文件，否则会无法生成文件
    fp.close()
