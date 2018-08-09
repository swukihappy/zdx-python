# -*- coding:utf-8 -*-
list_1={"name":"xiaoming","yuwen":2,"shuxue":3,"huaxue":3}
list_2={"name":"zdx","yuwen":1,"shuxue":3,"huaxue":1}
list_3={"name":"cgx","yuwen":2,"shuxue":3,"huaxue":3}
yuwen,shuxue,huaxue=3,5,10
list=[list_1,list_2,list_3]
list_sum=[]
for data in list:
	dir_sum={}
	dir_sum["name"]=data["name"]
	dir_sum["money"]=data["yuwen"]*yuwen+data["shuxue"]*shuxue+data["huaxue"]*huaxue
	print(dir_sum)
	list_sum.append(dir_sum)
print(list_sum)