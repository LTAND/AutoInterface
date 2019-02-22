import pytest
import json
from common.ReadExcel import ReadExcel
from common.SendRequest import Request


def make_response():
    Params = []
    reps = []
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


        # 传参请求数据
        reps.append({
            'rowNum': sheet_data[i]['Url'],
            'Id': sheet_data[i]['Id'],
            'Name': sheet_data[i]['Name'],
            'Url': sheet_data[i]['Url'],
            'Method':sheet_data[i]['Method'],
            'Headers': sheet_data[i]['Headers'],
            'Params': Params[i],
            'Status_code':sheet_data[i]['Status_code'],
            'Code':sheet_data[i]['Code']
        })
    return reps


# 读取Excel数据
filepath = r"dataExcel/02.xls"    # Excel文件路径
sheetName = "Sheet1"        # 表名
sheet = ReadExcel(filepath, sheetName)  # 模块.类名
sheet_data = sheet.readExcel()
data = make_response()  # 存放表格每一行请求参数

class Test_api_pytest:

    @pytest.mark.parametrize("data", data)
    def test_check(self, data):
        r = Request(
            data['Url'],
            data['Method'],
            data['Headers'],
            data['Params'],
            data['Status_code'],
            data['Code']
        )
        js_re = r.getJson()
        
        # 表格设置的检查点
        dict_Code = json.loads(data['Code'])
        code_first_key = str(list(dict_Code.keys())[0])
        code_first_value = str(list(dict_Code.values())[0])

        # assert int(data['Status_code']) == int(js_re.get('status')) # 断言请求状态

        print("用例编号:", data['Id'], "\n用例名称:", data['Name'], '\n请求地址:',data['Url'])
        print("Code检查点:", dict_Code)
        print('响应数据:\n', json.dumps(js_re, sort_keys=False, indent=4, ensure_ascii=False))
            
        assert code_first_value == str(js_re.get(code_first_key))
        
if __name__ == "__main__":
    pytest.main(['--html=./report/report.html', 'run.py'])
    pass

# pytest run.py -s -v
# pytest run.py --html=report/report.html
