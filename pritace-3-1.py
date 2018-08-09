# -*- coding:utf-8 -*-
l1="abcdefg"
l2="dfgvefgh"
def find_str(str1,str2):
	l3=[]
	for x in str1:
		if x in str2:
			l3.append(x)
	return l3
str3=find_str(l1,l2)
print(str3)
print(find_str(["qwe","1"],"1"))
def func():
	x=3
	action=(lambda n:x**n)
	return action
x=func()
print(x(4))
def makeActions():
	acts=[]
	for i in range(5):
		acts.append(lambda x ,i=i:i **x)
	return acts
acts=makeActions()
print(acts[2](3))
print(acts[1](3))
def f1():
	x=99
	def f2():
		def f3():
			print(x)
		f2()
		f3()
print(f1())