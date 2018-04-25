# -*- coding : utf-8 -*-
sum=0
n=101
while n>1:
	n=n-2;
	sum=sum+n
	
print("1+3+5+..+99=%d" %sum)

L=["Bart","Lisa","Adam"]
for name in L:
	print("hello,%s" %name)

i=0;
while i<3:
	print("hello,%s" %L[i])
	i=i+1
