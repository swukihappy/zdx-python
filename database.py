# -*- coding:utf-8 -*-
import pymysql as mdb
con=None
con=mdb.connect("localhost","root","123456","zdxpractice",3306)
cur=con.cursor()
cur.execute("select * from mybook")
date=cur.fetchall()
print(date)
l=[]
for x in date:
	my_dir={}
	my_dir["name"]=x[1]
	my_dir["count"]=x[2]+x[3]+x[4]
	l.append(my_dir)
print(l)
for i in l:
	cur.executemany("insert into my_count(name,suma) value (%s,%s)",[[i["name"],i["count"]]])
con.commit()
cur.close()