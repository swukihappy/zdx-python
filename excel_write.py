# -*- coding:utf-8
import xlwt
import re
file_path=r"C:\Users\swuki\Desktop\my2book.xls"
data=xlwt.Workbook(file_path)
table=data.add_sheet("mypractice")
table.write(0,1,"happy")
data.save(file_path)