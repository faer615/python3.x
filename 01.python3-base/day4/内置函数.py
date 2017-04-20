#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh

# all() # 除了0 都为真
# any() # 有返回值 为真
# bin() # 数字转成2进制
# bool() # 判断布尔值 有为真 没有为假
# filter() # 过滤结果
res = filter(lambda n:n>5,range(10))
for i in res:
    print(i)

print("====================")
mas = map(lambda n:n*n,range(10))
for i in mas:
    print(i)

# 所有数字累加
import functools
com = functools.reduce( lambda x,y:x+y,range(100))
print(com)

print(globals()) # 打印当前代码所有内容