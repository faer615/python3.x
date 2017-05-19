#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: UDP socket 客户端

import socket

addr = ('127.0.0.1',8200)
# AF_INET说明使用IPv4地址，SOCK_DGRAM指定UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg = input("输入消息：")
    msg = bytes(msg, encoding="utf8")  # 客户端将byte数据转换成 utf8编码发送
    s.sendto(msg,addr)
#    s.sendto("Received: ",bytes(msg, encoding="utf8"),addr)
    if msg=='bye':
        break
s.close()