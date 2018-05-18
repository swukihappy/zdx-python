# -*- coding:utf-8 -*-
class Zdx(object):
	def __init__(self,name,age):
		self.__name=name
		self.__age=age
	def my_print(self):
		print(self.__name,self.__age)
	def getname(self):
		return self.__name
zdx1=Zdx("zhang",12)
zdx1.my_print()
print(zdx1.getname())
print(zdx1._Zdx__name)
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
            return self.__gender
    def set_gender(self,gender):
        self.__gender=gender
 # 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
