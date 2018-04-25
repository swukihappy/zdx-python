# -*- coding -*-
# 判断一个对象是否是可迭代对象
from collections import Iterable
a=isinstance("zhangdongxue",Iterable)
print(a)

for i,value in enumerate("zhangdongxue"):
	print(i,value)