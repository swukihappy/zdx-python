# -*- coding:utf-8 
#从数据库读取数据，写入excel表格，
import pymysql as mdb
import xlwt as xl
import xlrd
import re
# 从数据库读取数据
con=mdb.connect("localhost","root","123456","zdxpractice",3306)
cur=con.cursor()
sql="select * from mybook"
cur.execute(sql)
date=cur.fetchall()
cur.close()
con.close()
# 写入excel表格
file_path=r"C:\Users\swuki\Desktop\zdxmybook.xls"
newfile=xl.Workbook(encoding="utf-8")
newsheet=newfile.add_sheet("mybook1")
for value in date:
	col=0
	while col <4:
		newsheet.write(date.index(value),col,str(value[col+1]))
		col=col+1
#newfile.save(file_path)

# 从表格中读取数据，写入数据库
file_path1=r"C:\Users\swuki\Desktop\zdxmybook1.xls"
my_excel=xlrd.open_workbook(file_path1)
my_sheet=my_excel.sheet_by_name("mybook1")
my_excel_nrows=my_sheet.nrows
l=[]
nrows=0
while nrows<my_excel_nrows:
	l.append(my_sheet.row_values(nrows))
	nrows=nrows+1
# print(l)
## 读取excel指定单元格数据
cell=my_sheet.cell(0,1).value
# 读取excel一列数据
ncols=my_sheet.col_values(1)
# .join(str)练习
l1=[]
for i in l:
	l1.append("".join(i))



