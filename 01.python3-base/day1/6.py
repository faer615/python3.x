#!/usr/bin/env python
#coding:utf8
#Author:Felix zheng
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
