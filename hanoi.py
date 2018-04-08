# -*- coding:utf-8 -*-
def mov(n,a,b,c):
	if n==1:
		print("%c-> %c" % (a,c))
	else:
		mov(n-1,a,c,b)
		print("%c->%c" % (a,c))
		mov(n-1,b,a,c)

mov(3,'A','B','C')