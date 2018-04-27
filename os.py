#!/user/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
file_path="D:\zdx1234.txt"
rat=os.access(file_path,os.F_OK)
print("文件路径存在么:{}".format(rat))
rat=os.access(file_path,os.R_OK)
print("文件可读么:{}".format(rat))
rat=os.access(file_path,os.W_OK)
print("文件可写么:{}".format(rat))
rat=os.access(file_path,os.X_OK)
print("文件可执行么{}".format(rat))

rat=os.access(file_path,os.R_OK|os.R_OK|os.W_OK|os.X_OK)
print(rat)

ret=os.getcwd()#获得当前工作目录
print(ret)
#修改当前工作目录
os.chdir("c:\\")
print(os.getcwd())