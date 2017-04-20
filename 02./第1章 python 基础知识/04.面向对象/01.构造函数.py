#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 构造函数

class MyClass(object):
    message = "Hello,Developer"

    def show(self):
        print(self.message)

    def __init__(self):
        print("Constructor is Called") # Constructor 构造函数

inst = MyClass()
inst.show()