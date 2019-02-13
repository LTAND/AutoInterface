## 目录结构
#### ExcelUtil.py 封装读取excel数据
#### RequUtil.py 封装请求
#### main.py 根据excel数据，打印请求后响应的数据
#### HTMLTestReportCN.py 生成html报告模板的库
#### dataExcel 储存的excel模板数据
#### reportHtml 存储html报告
## 1. 下载库
#### pip install requests
#### pip install xlrd
#### pip install unittest

## 2. 按dataExcel/02.xls例子填写表格信息
#### Params填写请求参数的个数 
#### 1-表示一个参数,可以容纳多个参数;
#### 0-表示无参数;
#### -1-表示参数为json参数,json里面"key":"value"要这样,

## 3.在test_HTMLTestReportCN.py中
#### 填写excel文件路径filepathl和excel里面的表名Sheet2
#### 填写生成html报告的标题，文件名路径, 描述, 执行者

## 4.运行脚本
```bash
cd AutoInterface
python test_HTMLTestReportCN.py
```
#### 生成后的html
![Alt text](reportHtml\img.jpg)