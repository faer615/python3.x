#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: json序列化01
import json # 简单转换

def sayhi(name):
    print("hello",name)

info = {
    'name':"felix",
    'age':22,
    'func':sayhi
}

f = open("json.txt","w")
#print(json.dump(info))
f.write(json.dumps(info))
f.close()