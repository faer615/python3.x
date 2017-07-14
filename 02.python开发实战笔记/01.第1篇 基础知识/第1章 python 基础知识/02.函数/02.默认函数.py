#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 默认函数

def sum(x, y = 10 ):
    return x+y

if __name__ == '__main__':
    print("return of sum(2, 3):", sum(2,3))
    print("return of sum(-4):", sum(-4))