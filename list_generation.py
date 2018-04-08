# -*- coding:utf-8 -*-
from collections import Iterable
import os
L=[x*2 for x in range(0,10) if x*2%4==0]
if (isinstance(L,Iterable))==True:
		print(L)
else:
	print("L is not an iterable")
M=[d for d in os.listdir('.')]
print(M)

L=["hello","world","IBM","APPLE"]
S=[s.lower() for s in L]

print(S)