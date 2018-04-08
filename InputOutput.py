# -*- coding:utf-8 -*-
str_1="zhangdongxue"
str_2="caigaoxing"
print(str(str_1))
print(repr(str_1 ))
for x in range(10):
	print(repr(x).ljust(4),repr(x*2).center(2),repr(x*x*x).rjust(2))
print("我的名字是{name},年龄是{age}".format(name="zhangdongxue",age=24))
str_1=input("请输入你的生日日期:")
print(str_1)