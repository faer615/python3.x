#!/usr/bin/env python
# coding: utf-8
# Author:Felix_zh
#Function: 记录日志时间

import time
def logger():
    time_format='%Y-%m-%d %X'
    time_current=time.strftime(time_format)
    with open('a.txt','a+') as f:
        f.write('%s end action\n' %time_current)

def tst11():
    print('test1 starting action...')

    logger()

def tst21():
    print('test2 starting action...')

    logger()

def tst31():
    print('test3 starting action...')

    logger()

tst11()
tst21()
tst31()