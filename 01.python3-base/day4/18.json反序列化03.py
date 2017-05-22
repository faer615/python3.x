#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: json序列化03
import json

f = open("pickle03.txt","r")
data = json.load(f)
print(data["age"])
