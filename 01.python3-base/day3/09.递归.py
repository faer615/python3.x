#!/usr/bin/env python
# coding: utf-8
# Author:Felix_zh
# 递归运算

def calc(n):
    print(n)
    if int(n/2) >0:
        return calc( int(n/2) )
    print("-->",n)

calc(10)