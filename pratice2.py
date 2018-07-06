# -*- coding:utf-8 -*-
### 第一题
print(2**16)
print(2/5)
print(2/5.0)
print("spam"+"eggs")
s="ham"
print("eggs"+s)
print(s*5)
print("green %s and %s" % ("eggs",s))
print(s[:0])
print("green {0} and {1}".format("eggs",s))
print(("x",)[0])
print(("x","y")[1])
L=[1,2,3]+[4,5,6]
print(L)
print(L[:])
print(L[:0])
print(L[-2])
print(L[-2:])
print(([1,2,3]+[4,5,6])[2:4])
print([L[2],L[3]])
L.reverse()
print(L)
L.sort()
print(L)
print(L.index(4))
print({"a":1,"b":2}["b"])
D={"x":1,"y":2,"z":3}
D["w"]=0
print(D["x"]+D["w"])
D[(1,2,3)]=4
print(list(D.keys()))
print(list(D.values()))
print((1,2,3) in D)
print(2 in D)
print([[]])
print(["",[],(),None])
L=[1,2,3,4]
print(L[3])
print(L[100:101])
L[2]=[]
print(L)
del L[0]
print(L)
del L[1:]
print(L)
for x in range(1,10):
	L.append(x)
print(L)
L[2:4]=[5,6]
print(L)
x="spam"
y="eggs"
x,y=y,x
print(x,y)
D={}
D[1]="a"
D[2]="b"
print(D)
## 第十题
L=[]
my_personal_info={"name":"zdx","ege":23,"work":"QA","address":"zkdy","email":"sw@163.com","tel":"15104506430"}
L.append(my_personal_info)
print(L)
### 第十一题
my_file=open(r"d:/zdxgit/myfile.txt","w")
my_file.write("Hello file world\n")
my_file.close()
my_read=open(r"d:/zdxgit/myfile.txt","r")

zdxstr=my_read.readline()
print(zdxstr)