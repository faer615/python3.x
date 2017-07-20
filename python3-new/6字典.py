#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2017/7/18 21:59
# @File    : 6字典.py
# @Author  : Felix-zh
# @E-mail  : chengfeng56@qq.com
# @Function: 字典 dict
'''
键：值
key:value
'''
# 创建一个字典
phone_book = {'Tom':123,'jerry':456,'king':789}
max_dict = {"Tom":'boy',11:23.5}

# 访问字典值
print("Tom has phone number: " + str(phone_book['Tom']))

# 修改字典值
phone_book['Tom'] = 999
print("Tom has phone number: " + str(phone_book['Tom']))

# 添加字典值
phone_book['Heath'] = 888
print("The added book is: " + str(phone_book))

# 删除字典值
del phone_book['Tom']
print("The book after del is: " + str(phone_book))

# 清空字典
phone_book.clear()
print("The book after clear is: " + str(phone_book))

# 删除字典
#del phone_book
#print("The book after del is: " + str(phone_book))

# 字典特性
# 同一个字典内键值只能有一个,多个值显示最后一个。
req_test = {'name':'abc', 'age':5, 'name':5}
print("req_test: " + str(req_test))

# 键不可变的，可以用数字，字符串，元组充当键，不能用列表。
list_dict = {('name'):'john','age':13}
print("list_dict is: " + str(list_dict))