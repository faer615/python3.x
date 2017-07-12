#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 字符串 单，双引号 多行注释

print("hello world!")
print('hello world!')
print('''
This is the first line
This is the second line
Last line
''')

age = 3
name = "Tom"
print("{0} was {1} years old".format(name,age))
print(name + " was " + str(age) + " years old")