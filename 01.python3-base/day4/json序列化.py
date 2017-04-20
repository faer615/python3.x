#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh
#import json # 可支持java
import pickle # 只支持python

def sayhi(name):
    print("hello2",name)

info = {
    'name':'felix',
    'age':26,
    'func':sayhi
}

f = open("test.text","wb")
f.write(pickle.dumps(info))

f.close()