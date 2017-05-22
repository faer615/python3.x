#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 迭代器

from  collections import Iterator
# 可以进行 for 循环的数据类型，
# 一类是集合数据类型，list、duple、dict、set、str等
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否Iterable对象
#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

# f.readlines # 读取文件每一行生成列表
