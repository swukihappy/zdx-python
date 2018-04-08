# -*- coding:utf-8 -*-
list_1=[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
]
list_2=[]
for i in range(4):
	list_row=[]
	for x in list_1:
		list_row.append(x[i])
	list_2.append(list_row)
print(list_2)
list_3=[[x[i] for x in list_2] for i in range(3)]
print(list_3)
del list_3[0]
print(list_3)