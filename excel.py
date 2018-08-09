# -*- coding:utf-8
import xlrd
import re
file_path=r"C:\Users\swuki\Desktop\mybook.xlsx"
data=xlrd.open_workbook(file_path)
table=data.sheet_by_index(0)
l=[]
r=0
while r<table.nrows:
	l_key={}
	l_key["name"]=table.cell(r,1).value
	l_key["yuwen"]=table.cell(r,2).value
	l_key["shuxue"]=table.cell(r,3).value
	l_key["huaxue"]=table.cell(r,4).value
	l.append(l_key)
	r=r+1
