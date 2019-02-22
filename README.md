## 目录结构
#### HTMLTestReportCN.py 生成html报告模板的库
#### ReadExcel.py 封装读取excel数据
#### SendRequest.py 封装请求
#### dataExcel 存储的excel模板数据xls
#### run.py 根据excel数据，打印请求后响应的数据
#### report 存储生成html报告

## 1. 下载库
#### pip install requests
#### pip install xlrd
#### pip install pytest

## 2. 按dataExcel/02.xls例子填写表格信息
![Alt text](https://github.com/LTAND/AutoInterface/blob/master/images/excel02_sheet1.jpg)

#### Params填写请求参数的个数 
#### 1-表示一个参数,可以容纳多个参数;
#### 0-表示无参数;
#### -1-表示参数为json参数,json里面{"key":"value"}要这样,

## 3.在run.py中
#### 填写excel文件路径filepathl和excel里面的表名Sheet2

## 4.运行脚本
```bash
  cd AutoInterface
  pytest run.py -s -v # 控制台打印信息
  pytest run.py --html=report/report.html # 生产html报告
```