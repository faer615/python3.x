#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh
# 除了单一字符串，整数，其他类型局部变量都可以修改

scholl = "New Edu"
names = ["Felix","Zheng","Jack"]
names_tuple = (1,2,3,4)

def change_name():
    names[0] = "小郑"
    print("inside func",names)

change_name()
print(names)