#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 私有成员

class MyClass(object):

    def __init__(self, name = "unset", color = "black"):
        print("Constructor is called with params: ",name, " ", color)
        self.__name = name
        self.__color = color

    def __del__(self):
        print("Destructor is called for %s!" % self.__name)

inst = MyClass("Jojo", "White")
del inst