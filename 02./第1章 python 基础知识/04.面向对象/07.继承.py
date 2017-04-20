#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 继承

class Base(object):
    def __init__(self):
        print("Constructor is Base is called !")

    def __del__(self):
        print("Move called in Base!")

    def move(self):
        print("move called in Base!")

class SubA(Base):
    def __init__(self):
        print("Constructor of SbuA is called !")

    def move(self):
        print("Move called in SubA !")

class SubB(Base):
    def __del__(self):
        print("Destructor of SubB is called !")
        super(SubB, self).__del__()

instA =SubA()
instA.move()
del instA

print("------------------------")

instB = SubB()
instB.move()
del instB