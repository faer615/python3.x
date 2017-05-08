#!/usr/bin/env python
#coding:utf8
#Author:Felix zheng
#Function: 加密输入密码
import getpass

_username = 'felix'
_password = 'king111'
username = input("用户名:")
password = input("密码:")
#password = getpass.getpass("password:") # 加密密码

if _username == username and _password == password:
    print("Welcome user {name} login ...".format(name=username))
else:
    print("Invalid username or password!")