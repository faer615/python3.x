#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh
# 生成器并行

import time
def consumer(name):
    print("%s 准备吃包子了！" %name)
    while True:
        baozi = yield

        print("[%s]包子上来了,被[%s]吃了！" %(baozi,name))

#c = consumer("小郑")
#c.__next__()

#b1 = "韭菜包子"
#c.send(b1)
#c.__next__()

def producer(name):
    c = consumer('小王')
    c2 = consumer('小李')
    c3 = consumer('小张')
    c.__next__()
    c2.__next__()
    c3.__next__()
    print("开始准备做包子！")
    for i in range(11):
        time.sleep(1)
        if i > 0:
            print("做了3个包子！")
            c.send(i)
            c2.send(i)
            c3.send(i)

producer("Felix")