#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh

import time

# 装饰器
def timer(func): # timeer(test1) func=test1
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs) # run test1()
        stop_time=time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return deco

@timer # test1=timer(test1)
def test1():
    time.sleep(1)
    print('in the test1')

@timer
def test2(name,age):
    time.sleep(1)
    print("test2:",name,age)

test1()
test2("Felix",26)