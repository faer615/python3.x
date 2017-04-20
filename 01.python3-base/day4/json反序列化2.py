#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh
#import json # 可支持java
import pickle # 只支持python

def sayhi(name):
    print("hello2",name)

f = open("test.text","rb")

#data = pickle.loads(f.read()) # 等同于
data = pickle.load(f)

print(data["func"]("Felix"))