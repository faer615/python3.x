#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: elif 语句

import sys

param = None

if len(sys.argv) > 1:
    param = int(sys.argv[1])

if param is None:
    print('Alert')
    print('The param is not set')
elif param < -10:
    print('The param is small')
elif param > 10:
    print('The param is big')
else:
    print('The param is middle')