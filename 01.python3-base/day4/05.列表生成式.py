#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 列表生成式

a = [1,2,3,4,5]
print(a)

b=[ i*2 for i in range(10) ]
print(b)
# 等于
a = []
for i in range(10):
    a.append(i*2)
print(a)