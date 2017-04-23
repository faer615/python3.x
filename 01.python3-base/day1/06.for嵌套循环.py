#!/usr/bin/env python
#coding: utf8
#Author: Felix
#E-mail: chengfeng56@qq.com
#Function: for嵌套循环

'''
for i in range(0,10):
    if i < 5:
        print("loop",i)
    else:
        continue
    print("hehe...")
'''
for i in range(10):
    print ('----------',i,'---------')
    for j in range(10):
        print(j)
        if j > 5:
            break
