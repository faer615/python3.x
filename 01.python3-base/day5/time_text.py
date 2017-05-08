#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Felix_zh
# E-mail:chengfeng56@qq.com
# Function: 时间戳转换为格式化本地时间
# gmtime：结果为UTC时区 localtime：结果为utc+8时区

import time

# 将时间戳转换为 strict_time(tuple)
x = time.localtime() #获取time.localtime()
print("x的方法有:\n",x)
# print(help(x))
print('今天是 %d年%d月%d日,%d时%d分%d秒' %(x.tm_year,x.tm_mon,x.tm_mday,x.tm_hour, x.tm_min, x.tm_sec))

# 将strict_time(tuple)转换为时间戳 time.mktime
print("将格式化时间转换为时间戳: " ,time.mktime(x),"秒")