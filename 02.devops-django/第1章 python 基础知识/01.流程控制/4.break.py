#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: break 跳出

count = 0
while True:
    input = raw_input("Enter quit: ")
    # check for valid passwd
    if input == "quit" :
        break
    count = count + 1
    if count%3 > 0:
        continue
    print("Please input quit!")
print("Quit loop successfully!")