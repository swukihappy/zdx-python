#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import codecs
import re

file_path = 'live-api.md'
result = []

in_param_section = False
item = {}
for line in codecs.open(file_path,'rb', 'utf-8'):
    line = line.strip('\n')
    if re.match('^###.*API.*', line):
        #把原来的item加到result里，然后新建一个item节点
        if item:
            result.append(item)
        item = {}
        item['name'] = line[12:].strip()
        item['params'] = []
        in_param_section = False
    elif re.match('https://api.baijiayun.com', line):
        item['url'] = line[len("https://api.baijiayun.com"):]
    elif re.match(u'^####.*【请求参数】.*', line):
        # 遇到请求参数这一行，把in_param_section设置为True，表示可以解析参数了，
        #也就是在这后面的表格参数需要解析，其它地方的不解析，在每个API起始的地方，把in_param_section重置为False
        in_param_section = True
    elif re.match('^\|[a-zA-Z0-9_` ]+\|.*$', line):
        if not in_param_section:
            continue
        # 这一行是参数，需要解析
        arr_line = line.replace('`', '').replace(' ', '').split('|')
        if len(arr_line) != 7:
            continue

        param = {}
        param['name'] = arr_line[1]
        param['type'] = arr_line[2]
        param['is_required'] = (arr_line[3] == u'是')
        item['params'].append(param)

    else:
    	if re.match('^###',line):
    		in_param_section = False


print(json.dumps(result, indent=4, ensure_ascii=False))