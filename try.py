# -*- coding:utf-8 -*-
while True:
	reply="1231q4"
	if reply=="stop":
		break
	try:
		num=int(reply)
	except:
		print("bad"*6)
	else:
		print(num)
	break