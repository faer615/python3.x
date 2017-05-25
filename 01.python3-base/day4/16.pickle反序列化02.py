#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: pickle序列化01
import pickle

def sayhi(name):
    print("hello",name)

f = open("pickle02.txt","rb")
data = pickle.load(f) # 等同于 data = pickle.loads(f.read())
print(data["func"]("felix"))
