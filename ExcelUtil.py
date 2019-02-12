# coding:utf-8
import xlrd
import json
class ExcelUtil():
    def __init__(self, filepath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(filepath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            c = 1 # 跳过第一行，从第二格开始
            for i in list(range(self.rowNum-1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i+2
                values = self.table.row_values(c)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                c += 1
            return r

if __name__ == "__main__":
    # 测试读取Excel
    filepath = r'20181022自动化接口3\02.xls'
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    # print(data.dict_data())
    # print(json.dumps(data.dict_data(), sort_keys=False, indent=4, ensure_ascii=False))

