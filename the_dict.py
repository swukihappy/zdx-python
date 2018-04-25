# -*- coding:utf-8 
list_a=[2,3]
trup_a=(1,2,3)
trup_b=(1,list_a)
set_a=set(trup_a)
set_b=set(list_a)
set_a.add(6)
set_b.add(6)
set_c=set_a &set_b
set_d=set_a | set_b


print(set_a)
print(set_b)
print(set_c)
print(set_d)
