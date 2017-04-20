#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 处理异常

try:
    result = 3/0
    print('this is never been called')
except:
    print("Exception happened")
finally:
    print("Process finished!")