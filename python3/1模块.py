#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2017/7/13 22:54
# @File    : 5.py
# @Author  : Felix-zh
# @E-mail  : chengfeng56@qq.com
# @Function: 模块

import os
import requests

print(os.getcwd())
print(os.getcwd())

r=requests.get("https://www.baidu.com")

print(r.url)
print(r.encoding)
print(r.text)