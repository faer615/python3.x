#!/usr/bin/env python
# coding:utf8
# Author:Felix_zh

# 运算方法模块调用
from __future__ import division

def jia(x, y):
    return x + y

def jian(x, y):
    return x - y

def cheng(x, y):
    return x * y

def chu(x, y):
    return x / y

operator = {"+": jia, "-": jian, "*": cheng, "/": chu}

def f(x,o,y):
    print(operator.get(o)(x,y))

first_number=input("first_number:")
bc_x=input("yunsuan:")
sec_number=input("sec_number:")

print(f)