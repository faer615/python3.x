#!/usr/bin/env python
#coding: utf-8
# Author:Felix_zh
# 进度条


f = open("word",'r+',encoding="utf-8") # 打开文件
count =0
for line in f:
    if count == 3:
#        count += 1
        break
    print(line.strip())
    count += 1


#print(f.tell())
#print(f.readline().strip())
#print(f.tell())
# 高效率 打印文件
#count = 0 # 计数器
#for line in f:
#    if count == 9: # 循环到9行时，开始从第10行打印
#        print('---------分割线-----------')
#        count += 1
#        continue
#    print(line.strip())
#    count += 1

'''
# 效率低　循环文件
for index,line in enumerate(f.readlines()): # 建立文件索引

    if index == 9: # 循环到第9行，从第10行开始打印
        print('-------------分割线-----------')
        continue
    print(line.strip()) #去掉空行

'''
# 打印前5行
#for i in range(5):
#    print(f.readline())
#print(f.fileno())
#print(f.encoding)
#print(f.flush())
#print(dir(f.buffer))
f.close