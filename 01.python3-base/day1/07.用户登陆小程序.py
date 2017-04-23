#!/usr/bin/env python
#coding: utf8
#Author: Felix
#E-mail: chengfeng56@qq.com
#Function: 用户登陆小程序

count = 0  # 计数器
username = "111"  # 登录用户名
userpassword = "111"  # 登录密码

# 读取黑名单用户
f = open("back_user", "r")
file_list = f.readlines()
f.close()

lock = []
name = input("登录用户名:")

# 判断用户是否在黑名单
for i in file_list:
    line = i.strip("\n")
    lock.append(line)
if name in lock:
    print("您的账号已锁定，请联系管理员。")
else:
    # 如果用户没有在黑名单，判断用户是否存在。
    if name == username:
        # 如果密码连续输错三次，锁定账号。
        while count < 3:
            password = input("登录密码：")
            if name == username and password == userpassword:
                print("欢迎 %s,回来！" % name)
                break
            else:
                print("账号密码不匹配")
                count += 1
        else:
            print("对不起，您的账号连续输错三次账号已锁定，请联系管理员。")
            f = open("back_user", "w+")
            li = ['%s' % username]
            f.writelines(li)
            f.close()
    else:
        print("用户名不存在，请输入正确的用户名。")