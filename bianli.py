# -*- coding:utf-8 -*-
import sys
print(sys.path)
dict_1={"name":"zhangdongxue","age":16,"city":"haerbin"}
for k,v in dict_1.items():
	print(k,v)
list_1=["zhangdongxue","caigaoxing","hahahah"]
list_2=["nv","nan","buzhidao"]
for index,value in enumerate(list_1):
	print(index,value)
for a,b in zip(list_1,list_2):
	print("what is your {0},It is {1}".format(a,b))