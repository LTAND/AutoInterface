# coding:utf-8
import ExcelUtil as readSheet
import RequUtil as request
import unittest
import ast

class test_sheet1(unittest.TestCase):
    # 设计测试用例
    def test_1_2_3(self):
        for i in range(0, len(reps)):
            try:
                # if reps[i].getJson()['status'] == 200:
                print("\n==================================================================================")
                print("用例编号:",sheet_data[i]['Id'],"\n用例名称:",sheet_data[i]['Name'],'\n地址:',sheet_data[i]['Url'])
                print('响应数据:\n',reps[i].getJson())
            except:
                 print(sheet_data[i]['Id'],sheet_data[i]['Name'],'请求出错')

if __name__ == '__main__':

    # 读取Excel数据
    filepath = r"20181022AutoInterface\02.xls"    # Excel文件路径
    sheetName = "sheet1"        # 表名
    sheet = readSheet.ExcelUtil(filepath, sheetName)
    sheet_data = sheet.dict_data()
    
    reps = []   # 存放表格每一行请求对象
    
    # 传递Excel数据请求参数
    for i in range(0, len(sheet_data)):
        reps.append(request.RequUtil(
            sheet_data[i]['Url'],
            sheet_data[i]['Method'],
            sheet_data[i]['Headers'],  
            sheet_data[i]['Params'],   
            sheet_data[i]['Status_code'],
            sheet_data[i]['Code']
        )) 
        # 测试每条请求响应数据
        # print('响应的数据:',reps[i].getJson())

    # 执行测试用例
    unittest.main()
