# -*- coding:utf-8 -*- 
import xlwt
import xlrd
import re
# 创建excel表格
my_excel=xlwt.Workbook()
first_sheet=my_excel.add_sheet("first_sheet")
first_sheet.write(1,2,"zdx")

# 格式化excel表格
font=xlwt.Font()
font.name="微软雅黑"
font.bold=True
font.underline=True
font.colour_index=2
font.italic=True
style_1=xlwt.XFStyle()
style_1.font=font
first_sheet.write(2,3,"123",style_1)
# 设置单元格宽度
first_sheet.col(1).width=5555
first_sheet.row(1).height=5555
my_excel.save(r"C:\Users\swuki\Desktop\zdx.xls")