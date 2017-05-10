#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh

# 合集基本操作

t = set([1,2,3])
s = set([11,13,13])

t.add('x') # 添加一项
s.update([10,23,26]) # 添加多项
t.remove(2) # 删除一项
print(t,'\n',s)

'''
len(s)
set的长度

x in s
测试x是否是s的成员

x not in s
测试x是否不是s的成员

s.issubset(t)
s <= t
测试是否s中的每一个元素都在t中

s.issuperset(t)
s >= t
测试是否t中的每一个元素都在s中

s.union(t)
s | t
返回一个新的set包含s和t中的每一个元素

s.intersection(t)
s & t
返回一个新的set包含s和t中的公共元素

s.difference(t)
s - t
返回一个新的set包含s中有但是t中没有的元素

s.symmetric_difference(t)
s ^ t
返回一个新的set包含s和t中不重复的元素

s.copy()
返回set “s”的一个浅复制

'''