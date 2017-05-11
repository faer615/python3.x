#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh

import time

def bar():
    time.sleep(3)
    print('in the bar')

# 高级函数
def test2(func):
    print(func)
    return func

bar=test2(bar)
bar() # run bar