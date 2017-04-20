#!/usr/bin/env python
#coding:utf8
#Author:Felix zheng
__author__ = "felix"

names = ["Xiaozheng","Liyang","Zhangheng","Gaojing","Yangzheng"]
names.append("Xuejing") # 追加到末尾
names.insert(1,"Fanghua") # 插入某个字段之前
names.insert(3,"Gaojing") # 插入某个字段之后
names[2] = "Wanghai" # 修改
names.remove("Xiaozheng") # 删除字段
del names[1] # 删除字段
#names.pop() # 默认删除最后一个

print(names.index("Zhangheng"))
print(names[names.index("Zhangheng")])
print(names.count("Gaojing"))

print(names)
names.reverse() # 翻转列表
print(names)
names.sort() # 排序
print(names)

names2= [1,2,3,4,5]
names.extend(names2) # 合并列表
print(names,names2)


#print(names[0],names[2])
#print(names[1:3]) # 切片
#print(names[-2:])