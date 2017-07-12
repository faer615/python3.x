#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: first one

import os
import requests

print(os.getcwd())
print(os.getcwd())

r=requests.get("https://www.baidu.com")

print(r.url)
print(r.encoding)
print(r.text)