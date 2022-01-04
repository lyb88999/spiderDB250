# -*- coding = UTF-8 #-*-
# @Time : 2021/12/15 2:05 下午
# @Author : 李宇博
# @File : testxlwt.py
# @SoftWare : PyCharm

import xlwt

workbook = xlwt.Workbook(encoding="UTF-8")      # 创建Workbook对象
worksheet = workbook.add_sheet("sheet1")     # 创建工作表
worksheet.write(0, 0, 'hello')    # (行,列，内容)
workbook.save("student.xls")
