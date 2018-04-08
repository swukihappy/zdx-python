# -*- coding:utf-8 -*-
from collections import Iterable
L=[x*x for x in range(0,11) if x%2==0]
print(L)
g=(x*x for x in range(0,11) if x%2==0)
if isinstance(g,Iterable)==True:
	for x in g:
		print(x)

# 菲波那切数列
def feibo(n):
	L=[]
	for max in range(0,n):
		if max==0 or max==1:
			L.append(1)
			print(L[max])
		else:
			L.append(L[max-1]+L[max-2])
			print(L[max])
	return L
feibo(8)
def hanni(n,a,b,c):
	if n==1:
		print("%c ==== %c" %(a,c))
	else:
		hanni(n-1,a,c,b)
		print("%c=====%c" %(a,c))
		hanni(n-1,b,a,c)
hanni(3,"A","B","C")
