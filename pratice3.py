# -*- coding:utf-8 -*-
s="zhangdongxue"
sum=0
l=[]
for x in s:
	# print(ord(x))
	sum=sum+ord(x)
	l.append(x)
# print(sum)
# print(l)
e=map(ord,s)
# print(e)
# 排序字典
keys=[]
dir_1={}
zdx_dir={"name":"zhangdongxue","age":11,"count":"beijing"}
for x in zdx_dir.keys():
	keys.append(x)
print(keys)
q=sorted(keys)
print(q)
for x in keys:
	dir_1[x]=zdx_dir[x]
	print(x,zdx_dir[x])
# 程序逻辑替换方案
L=[1,2,3,4,8,16,32,64]
x=5
for i in L:
	for x in range(6):
		if i==2**x:
			print(i)
		else:
			pass

