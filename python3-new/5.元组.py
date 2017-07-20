#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2017/7/15 13:20
# @File    : 5元组.py
# @Author  : Felix-zh
# @E-mail  : chengfeng56@qq.com
# @Function: 元组实例
'''
创建
访问
删除
脚本操作符
函数方法
'''
# 创建包含只有一个元素的元组
a_tuple = (2,)

# 元组中包含列表
mixed_tuple = (1, 2, ['a', 'b'])

print("mixed_tuple: " + str(mixed_tuple))

mixed_tuple[2][0] = 'd'
mixed_tuple[2][1] = 'f'

print("mixed_tuple after: " +str(mixed_tuple))

