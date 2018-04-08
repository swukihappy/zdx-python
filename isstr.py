# -*- coding:utf-8 -*-
L1=["Hello","World",18,"Apple",None]
for x in L1:
	if isinstance(x,str)==True:
		print(x)
		y=x.lower()
		print(y)

L2=[s.lower() for s in L1 if isinstance(s,str)==True]
print(L2)
