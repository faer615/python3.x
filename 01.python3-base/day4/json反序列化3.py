#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh
import json # 可支持java
#import pickle # 只支持python

f = open("test.text","r")

data = json.loads(f.read())

print(data)