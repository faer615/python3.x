#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 匿名函数

import datetime

def nameFunc(a):
    return "I'm named function with param %s" % a

def call_func(func, param):
    print(datetime.datetime.now())
    print(func(param))
    print("")

if __name__ == '__main__':
    call_func(nameFunc, 'hello')
    call_func(lambda x: x*2, 9)
    call_func(lambda y: y*y, -4)