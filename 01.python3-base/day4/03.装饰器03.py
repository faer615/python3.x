#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 高阶函数

import time
def timer(func): #timer(ts1) func=ts1
    def deco(*args,**kwargs): # 非固定参数
        start_time=time.time()
        func(*args,**kwargs)  #run ts1
        stop_time=time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return deco

@timer # 等于 ts1=timer(ts1) 装饰器
def ts1():
    time.sleep(1)
    print('in the ts1')

@timer
def ts2(name,age): # 非固定参数
    print("ts2：",name)

ts1()  # deco
ts2("felix",22)