#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function:
import time

x = time.localtime()
# strftime 转换为 strptime 格式化字符窜
print(time.strftime("%Y-%m-%d %H:%M:%S",x))

# strptime 转换为 strftime
print(time.strptime('2017-05-08 10:52:35',"%Y-%m-%d %H:%M:%S"))

