#!/usr/bin/env python
# -*- coding:utf8 -*-
# @author:许安
# @time：2017/1/15 20:30
# @Function: 将文档中的字符出现的次数进行统计

adict = {}
path = "randlist.txt"
a = ''.join(open(path).read().decode("utf-8"))
b = set(a)

#方法一：按key排序:
for line in b:
	adict[a.count(line)] = line

for key in sorted(adict.keys()):
	print key, adict[key]

#方法二：按照value排序：

# for line in b:
# 	adict[line] = a.count(line)
# 	print sorted(adict.items(), lambda x, y: cmp(x[1], y[1]))
