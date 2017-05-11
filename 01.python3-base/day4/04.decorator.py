#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: decorator装饰器 终极版 登陆验证

import time,datetime
user,passwd = 'xiao','111'
def auth(auth_type):
#    print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
#            print("wrapper func args:", *args, **kwargs)
            if auth_type == "local":
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                if user == username and passwd == password:
                    print("\033[32;1m User has passed local authentication \033[0m")
                    res = func(*args,**kwargs)
                    print("\033[35;1m ---after authentication--- \033[0m")
                    return res
                else:
                    exit("\033[31;1m Invalid username or password wrong \033[0m")
            elif auth_type == "ldap":
                print("\033[35;1m LDAP功能开发中 \033[0m")
        return wrapper # 包装
    return outer_wrapper
0
def index():
    print("\033[32;1m Welcome to Index page \033[0m")

@auth(auth_type="local")
def home():
    print("\033[33;1mWelcome to Home page \033[0m")
    # 将时间戳转换为 strict_time(tuple)
    x = time.localtime() #获取time.localtime()
    a=('亲爱的',user, '现在时间是 %d年%d月%d日,%d时%d分%d秒' %(x.tm_year,x.tm_mon,x.tm_mday,x.tm_hour, x.tm_min, x.tm_sec))
    return a

@auth(auth_type="ldap")
def bbs():
    print("Welcome to BBS page")

index()
print(home())
bbs()