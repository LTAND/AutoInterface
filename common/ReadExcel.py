#! /usr/bin/env python
# -*- coding:utf-8 -*-
import xlrd
import json
class ReadExcel():
    def __init__(self, filepath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(filepath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def readExcel(self):
        data = self.data
        table = self.table

        # 获取总行数、总列数
        nrows = self.rowNum
        ncols = self.colNum
        if nrows > 1:
            # 获取第一列的内容，列表格式
            keys = table.row_values(0)
            keys.insert(0, "rowNum")  # 添加行号字段
            # print(keys)

            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, nrows):
                values = table.row_values(col)
                values.insert(0, col+1)  # 添加行号值

                # keys，values这两个列表一一对应来组合转换为字典
                api_dict = dict(zip(keys, values))
                # print(api_dict)
                listApiData.append(api_dict)

            return listApiData
        else:
            print("表格未填写数据,总行数小于1")
            return None


if __name__ == '__main__':
    s = ReadExcel(r"dataExcel/02.xls", "Sheet1").readExcel()
    print(json.dumps(s, sort_keys=False, indent=4, ensure_ascii=False)) # 打印json化