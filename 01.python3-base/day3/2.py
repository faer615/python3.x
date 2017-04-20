#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh

# 集合 去重
list_1 = [1,3,5,6,7,10,20,6]
list_1 = set(list_1)

list_2 = set([2,4,6,8,9,10,20,7])
print (list_1,list_2)

# 交集 查找两个列表相同
print(list_1 & list_2)

# 并集 两个列表去重 union
print(list_1 | list_2)

# 差集 打印 列表1有，列表2没有 difference
print(list_1 - list_2)

# 子集 subset
list_3 =set([7,10,20])
print(list_3.issubset(list_1))

# 父集 upperset
print(list_1.issuperset(list_3))

# 对称差集 两个列表都没有的
print(list_1 ^ list_2)

print("-----------------------------------------")
list_4 = set([10,12,13])
# 显示列表是否有交集
print(list_3.isdisjoint(list_4))
