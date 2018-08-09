# -*- coding:utf-8 -*-
import pymysql as mdb
import random
con=mdb.connect("localhost","root","123456","zdxpractice",3306)
cur=con.cursor()
i=0
sql="insert into mybook(name,yuwen,shuxue,huaxue) value(%s,%s,%s,%s)"
while i<100:
	mybook={}
	i+=1
	name="name"+str(i);
	mybook["name"]=name
	mybook["yuwen"]=random.randint(1,10)
	mybook["shuxue"]=random.randint(1,10)
	mybook["huaxue"]=random.randint(1,10)
	cur.execute(sql,[mybook["name"],mybook["yuwen"],mybook["shuxue"],mybook["huaxue"]])
con.commit()
cur.close()
con.close()