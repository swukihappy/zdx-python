# -*- coding -*-
def findMinAndMax(l):
	if len(l)==0:
		return
	elif len(l)==1:
		str="只有一个元素哦"
		return str
	else:
		max= 0
		min= 0
		for i in l:
			print (i)
			if not isinstance(i,int):
				continue
			if i>max:
				max=i
			if i<min:
				min=i
		return min,max
l1=[1,2,3,4,5,6,7,8,9]
l2=[]
l3=[2]
l4=["sda","sdsa",1,2,"io",9,34]
print(findMinAndMax(l1))
print(findMinAndMax(l2))
print(findMinAndMax(l3))
print(findMinAndMax(l4))
