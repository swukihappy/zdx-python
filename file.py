# -*- coding:utf-8 -*-
with open("d:/zdx1234.txt","rb+") as f:	

	print(f.tell())
	f.seek(1,0)
	print(f.tell())
f.close()