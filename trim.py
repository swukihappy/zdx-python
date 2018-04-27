# -*- coding -*-
def trim(s):
	if len(s)==0:
		return s
	elif s[0]==" ":
		return trim(s[1:])
	elif s[-1]==" ":
		return trim(s[:-1])
	else:
		return s
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')