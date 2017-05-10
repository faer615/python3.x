#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 定义函数

import time

def bar():
    time.sleep(3)
    print('in the bar')

# 高阶函数
def test1(func):
    start_time=time.time()
    func() # run bar
    stop_time=time.time()
    print("the func run time is %s" %(stop_time-start_time))

test1(bar)