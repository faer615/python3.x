#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: python支持的数据类型
'''
numerices 数字
sequences 序列
mappings 映射
classes 类
instances 实例
exceptions 例外
'''
import sys

a = 3
b = 4

c =5.66
d = 8.0

e = complex(c,d) # 构造函数 复数
f = complex(float(a),float(b)) # 整形转为浮点型

print("a is type: ", type(a))
print("c is type: ", type(c))
print("e is type: ", type(e))

print(a + b)
print(d / c)

print(b / a)
print(b // a) # // 约等于
print(e)
print(e + f)

print(sys.float_info) # 查看系统支持的数据范围