#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh
# 修改文件
f = open("word","r",encoding="utf-8") # 以读取方式打开第一个文件
f1 =open("word.bak","w",encoding="utf-8") # 以写入方式打开第二个文件

for line in f: # 循环读取
    if "肆意的快乐" in line: # 判定关键字
        line = line.replace("肆意的快乐等我享受","肆意的快乐等着Felix享受") # 进行替换
    f1.write(line) # 写入文件
f.close()
f1.close()