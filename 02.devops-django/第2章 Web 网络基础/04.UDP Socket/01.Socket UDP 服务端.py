#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: UDP socket 服务端

import socket

addr=('',8200)
# AF_INET说明使用IPv4地址，SOCK_DGRAM指定UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(addr)

while True:
    data,addr=s.recvfrom(2048)
    data=str(data, encoding="utf8")  # 服务端将接收到的bytes数据 转换成 utf8编码
#    print("Received: ", redata)
    if data=='bye':
        print('client has exit')
        break
    print('received:',data," from",addr)
s.close()