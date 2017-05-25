#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: json序列化01
import json

f = open("json.txt","r")
data = json.loads(f.read())
print(data["age"])
