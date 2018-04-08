# -*- coding:utf-8 -*-
from collections import deque
list_1=["zhangdongxue","caigaoxing","hahahah","ukin"]
list_2=["zhao","qian","sun","li","zhou","wu","zheng","wang"]
list_3=[1,3,2,4,5,6,2,3]
list_1.append("大傻子")
print(list_1)
list_1.extend(list_2)
print(list_1)
print(len(list_2))
list_1.insert(1,"张冬雪")
print(list_1)
list_1.remove("zhao")
print(list_1)
print(list_1.pop())
print(list_1)
print(list_1.pop(1))
print(list_1.index("caigaoxing"))
print(list_1.count("caigaoxing"))
print(list_1)
list_3.reverse()
print(list_3)
print(list_1)

queue=deque(list_1)
queue.append("1")
print(queue)
print(queue.popleft())

