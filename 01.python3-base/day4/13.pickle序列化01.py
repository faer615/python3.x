#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: pickle序列化01
import pickle # 简单转换

def sayhi(name):
    print("hello",name)

info = {
    'name':"felix",
    'age':22,
    'func':sayhi
}

f = open("pickle.txt","wb")
#print(pickle.dumps(info))
f.write(pickle.dumps(info))
f.close()