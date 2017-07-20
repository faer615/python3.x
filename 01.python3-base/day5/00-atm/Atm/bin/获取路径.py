#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 获取路径
import os
import sys

print(os.path.abspath(__file__))  # 获取当前路径
print(os.path.dirname( os.path.abspath(__file__))) # 上层目录
BASE_DIR = os.path.dirname(os.path.dirname( os.path.abspath(__file__))) # 上层目录
# 加载相对路径
sys.path.append(BASE_DIR)
# 加载conf目录下文件 setting
from conf import settings
# 加载core目录下文件 main
from core import main

main.run()              # 执行程序