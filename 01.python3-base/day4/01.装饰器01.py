#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 装饰器

import time

# 装饰器 高阶函数
def timer(func): # timer(zs1) func=zs1
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs) # run zs1()
        stop_time=time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return deco

@timer # test1=timer(zs1)
def zs1():
    time.sleep(1)
    print('in the zs1')

@timer
def zs2(name,age):
    time.sleep(1)
    print("zs2:",name,age)

zs1()
zs2("Felix",26)