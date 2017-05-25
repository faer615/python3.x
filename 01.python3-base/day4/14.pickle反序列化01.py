#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: pickle序列化01
import pickle

def sayhi(name):
    print("hello",name)

f = open("pickle.txt","rb")
data = pickle.loads(f.read())
print(data["func"]("felix"))
