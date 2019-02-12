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
                 print("用例编号:",sheet_data[i]['Id'],"用例名称:",sheet_data[i]['Name'],'请求出错')

# class test_sheet2(unittest.TestCase):

#     def test_bbs(self):
#         for i in range(0, len(reps)):
#             try:
#                 print("\n==================================================================================")



#             except:
#                 print("用例编号:",sheet_data[i]['Id'],"用例名称:",sheet_data[i]['Name'],'请求出错')

if __name__ == '__main__':

    # 读取Excel数据
    filepath = r"D:\vsworkspace\2018年10月\20181022自动化接口2\02.xls"    # Excel文件路径
    sheetName = "Sheet2"        # 表名
    sheet = readSheet.ExcelUtil(filepath, sheetName)
    sheet_data = sheet.dict_data()
    
    reps = []   # 存放表格每一行请求对象
    Params = []
    # 传递Excel数据请求参数
    for i in range(0, len(sheet_data)):
        keys = []      # 存放参数名 eg：type
        values = []    # 存放参数值 eg：huitongkuaidi
        ParamsNum = int(sheet_data[i]['Params'])  # 每行的参数个数   eg：2 
        if ParamsNum > 0:
            for x in range(1, ParamsNum+1):                 # 遍历当前行的每个参数   
                curList = sheet_data[i]['Parameter'+str(x)].split("=")      # 当前行的当前参数  eg：type=huitongkuaidi
                keys.append(str(curList[0]))                                      
                values.append(str(curList[1]))
                Params.append(dict(zip(keys,values)))
                # 测试打印当前参数
                # print(curList[0],curList[1])
                # print(dict(zip(keys,values)))
                # print(Params[i])
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
    
    # 执行测试用例
    unittest.main()
