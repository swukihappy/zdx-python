# -*-coding:utf-8 -*_
#函数定义及调用,必须参数,关键字参数,默认参数,不定长参数,匿名函数
#return 语句

#必须参数
def fun_bixucanshu(str):
	print(str)
	return
#关键字参数
def fun_guanjianzi(str):
	print(str)
	return
#默认参数
def fun_defult(name,age=24):
	print(name,age)
	return
#不定长参数
def fun_budingchang(name,*var_arges_tuple):
	print(name)
	for x in var_arges_tuple:
		print(x)
	return
#匿名函数
sum=lambda arg1,arg2:arg1 + arg2
#return 语句
def fun_return(a,b):
	c=a+b
	return c
total=0	
def local_var(a,b):
	total=a+b
	return total

print(total)
print(sum(10,20))
print("必须参数:")
fun_bixucanshu("zhangdongxue")
print("关键字参数:")
fun_guanjianzi(str="caigaoxing")
print("默认参数")
fun_defult(name="hahha")
fun_defult("hehheh",20)
print("不定长参数:")
list_name=["zhao","qiao","sun","li"]
fun_budingchang(list_name,"zhang")
print("匿名函数")
print(sum(10,20))
#return 语句
print("return语句")
print(fun_return(1,2))
print(dir())