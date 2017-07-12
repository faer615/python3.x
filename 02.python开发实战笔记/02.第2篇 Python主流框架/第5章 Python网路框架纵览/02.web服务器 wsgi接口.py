#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: wsgi接口 适用于python2.7

# 全称 Web Server Gateway Interface 也可称作为 Python Web Server Gateway Interface 开始于2003年

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<b>Hello World !</b>'

from  wsgiref.simple_server import make_server
from webapp2 import application

server = make_server('',8080,application)
server.serve_forever()