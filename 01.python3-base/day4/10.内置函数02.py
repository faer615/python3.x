#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh

#函数赋值
def say(n):
    print(n)
say(3)

print("++++++++++++++++++++++++")
# 匿名函数赋值
calc = lambda n:print(n)
calc(5)

print("++++++++++++++++++++++++")

# 过滤合格匿名函数 打印大于5的值
res = filter(lambda n:n>5,range(10))
for i in res:
    print(i)

print("++++++++++++++++++++++++")
# map 函数 生成新的列表 n乘以10的列表
mma = map(lambda n:n*2,range(10)) # 等同于 [i*2 for i in range(10)]
for i in mma:
    print(i)

# 列表生成式
lis = [lambda x:x*2 for x in range(10)]
for x in lis:
    print(x)

print("++++++++++++++++++++++++")
# 依次相加列表数值
import functools
jia = functools.reduce( lambda x,y:x+y,range(10))
print(jia)

print("字典")
a = {6:2,8:0,1:4,-5:6,99:11,4:22}

# 按照key排序
print(sorted(a.items()))

# 按照 vaule 排序
print(sorted(a.items(),key=lambda x:x[1]))

# 默认无序打印
print(a)

# 合并变量
a = [1,2,3,4,5]
b = ['a','b','c','d','e']

for i in zip(a,b):
    print(i)

# 根据名称导入模块
#import decorator
__import__('decorator')

# 只打印全局变量
#def fsd():
#    local_var = 333
#    print(locals())
#fsd()
#print(globals())
#print(globals().get('local_var'))