# -*- coding:utf-8 -*-
import math
def my_isinstance(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')

def quadratic(a,b,c):
	for x in (a,b,c):
		my_isinstance(x)
	x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
	x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
	return x1,x2
print(quadratic(2,3,1))
print(quadratic(1,3,-4))
print(quadratic("aa",1,2))