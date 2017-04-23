#!/usr/bin/env python
#coding: utf8
#Author: Felix
#E-mail: chengfeng56@qq.com
#Function: 列表取值
# 浅 copy
import copy

person = ['name',['a',100]]

'''
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)
'''

p1 = person[:]
p2 = person[:]

p1[0] = 'zheng'
p2[0] = 'wang'
p1[1][1]=50

print(p1)
print(p2)
print('-----------------')