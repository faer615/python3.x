#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 多个异常

try:
    myList= [4, 6]
    print(myList[10])
    print("This is never been called")
except ZeroDivisionError as e: # ,适用于2.7版本
    print("ZeroDivisionError Happened")
    print(e)
except (IndexError, EOFError) as e:
    print("Exception happened")
    print(e)
except:
    print("Unknow exception happened")
else:
    print("No exception happened!")
finally:
    print("Process finished!")