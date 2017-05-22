#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: json序列化02
import json

def sayhi(name):
    print("hello",name)

info = {
    'name':"felix",
    'age':22,
#    'func':sayhi
}

f = open("pjson03.txt","w")
f.write(json.dumps(info))

info['age'] = 23
f.write(json.dumps(info))

f.close()