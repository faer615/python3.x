#!/usr/bin/env python
# coding: gbk
# Author:Felix_zh
#import sys
#print(sys.getdefaultencoding())

s = "你好"
s_gbk = s.encode("gbk")
print(s_gbk)
print(s.encode())

gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")
print("utf8",gbk_to_utf8)
print(gbk_to_utf8)
