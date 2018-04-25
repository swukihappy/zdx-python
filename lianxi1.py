# -*- coding:utf-8 -*-
L1=["ajdfkl","hdkal"]
def fun_1(list_name):
	list_name=list_name[0].upper()+list_name[1:].lower()
	return list_name
l2=list(map(fun_1,L1))
print(l2)