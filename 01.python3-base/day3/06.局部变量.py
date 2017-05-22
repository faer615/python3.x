#!/usr/bin/env python
# coding: utf-8
# Author:Felix_zh
# 局部变量

def change_name(name):
    print("before change",name)
    name ="Felix zh" # 作用域里生效
    print("after change",name)

name ="Wang"
change_name(name)
print(name)
