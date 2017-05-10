#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh
# 认证
import time

user,passwd='xiao','king111'
def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            print("wrapper func args:",*args,**kwargs)
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and passwd == password:
                    print("\033[32;1m User has passwd authentication \033[0m")
                    res = func(*args,**kwargs) # for home
                    print("---after authentication")
                    return res
                else:
                    exit("\033[31;1m Invalid username or password \033[0m")
            elif auth_type == "ldap":
                print("功能开发中。。。")
        return wrapper
    return outer_wrapper

def index():
    print("welcome to index page")

@auth(auth_type="local")
def home():
    print("welcome to home page")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page")

index()
print(home())
bbs()