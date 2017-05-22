#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 内置方法

print("all  除了0 都为真",all([1,-3])) #
print("any 有返回值为真")

a=(ascii([1,2,'小郑']))
print(type(a),[a])

print("10进制转2进制",bin(255))
print("有值为真，0为假",bool(1))

b=bytes("abcde",encoding="utf-8")
c=bytearray("abcde",encoding="utf-8")
print(b.capitalize(),"首字母大写")
print(c[1])
c[1]=58 # 重新赋值
print(c)

print("callable 判断是否看可以调用",callable([]), )
print("chr 返回ascii对应78位置的值",chr(78))
print("ord 返回ascii对应a的数字",ord('a'))

# lambda 函数
calc = lambda n:3 if n<4 else n
print(calc(2),'new')

print("====================")

res = filter(lambda n:n>5,range(10))
for i in res:
    print(i)

print("====================")
# 求自己平方
mas = map(lambda n:n*n,range(10))
for i in mas:
    print(i)

print("====================")

# 所有数字累加
import functools
com = functools.reduce( lambda x,y:x+y,range(100))
print(com)
# print("====================")
#
# print(globals()) # 打印当前代码所有内容

# 散列 hash
print(hash("felix"))
# 16进制
print(hex(255))

