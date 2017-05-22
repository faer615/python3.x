#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: pickle序列化02
import pickle

def sayhi(name):
    print("hello",name)

info = {
    'name':"felix",
    'age':22,
    'func':sayhi
}

f = open("pickle02.txt","wb")
pickle.dump(info,f)  # 等同于 f.write(pickle.dumps(info))
f.close()