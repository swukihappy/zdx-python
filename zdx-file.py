# -*- coding:utf-8 -*-
import re
file_path=r"D:\zdx-file\zdx.txt"
zdx_file=open(file_path,"r")
L=[]
for line in zdx_file.readlines():
	line.rstrip()
	L.append(line)
print(L)
K=[]
for w in L:
	K.append(w.rstrip())
s=",".join(K)
print(s)