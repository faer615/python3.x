#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 析构函数

class MyClass(object):
    message = 'Hello, Developer.'

    def show(self):
        print(self.message)

    def __init__(self,name = "unset", color = "black"):
        print("Constructor is called with params: ",name, " ", color)

    def __del__(self):
        print("Destructor is called!")

inst = MyClass()
inst.show()

inst2 = MyClass("David")
inst2.show()

del inst, inst2

inst3 = MyClass("Lisa", "Yellow")
inst3.show()

del inst3
