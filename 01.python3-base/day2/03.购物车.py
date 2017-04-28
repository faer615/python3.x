#!/usr/bin/env python
#coding: utf8
#Author: Felix
#E-mail: chengfeng56@qq.com
#Function: 购物车

shopping_list = [
        ['Iphone 6s plus',5800],
        ['Lumia',3800],
        ['Charge',45],
        ['Data line',35],
        ['MI 5 PRO',2299],
        ['MX4',1999],
]
salary = 100000
total = 0
shop_list = []

while True:
    welcome_1 = "欢迎使用XXX购物商城"
    we_1 = welcome_1.center(30,'*')
    print(we_1)
    choice_1 = "1.注册 2.登陆 q.退出"
    ch_1 = choice_1.center(32,'*')
    exit_1 = "谢谢使用，欢迎下次光临"
    ex_1 = exit_1.center(30,'*')
    error_1 = "您输入的用户已存在，请重新输入"
    e_1 = error_1.center(30,'-')
    error_2 = "密码不能为空，请重新输入"
    e_2 = error_2.center(30,'-')
    error_3 = "您输入的密码太短，请重新输入"
    e_3 = error_3.center(30,'-')
    error_4 = "您的输入有误, 请重新输入"
    e_4 = error_4.center(26,'*')
    error_5 = " 您的账号已被锁定，请联系管理员 "
    e_5 = error_5.center(12,'*')
    print(ch_1 )
    sr_1 = input("选择功能:")
    if sr_1 == '1':
        while True:
            with open('ming.txt','r')as r_1:
                temp = r_1.readlines()
                print (temp)
                tlist = []
            for tline in temp:
                tline = tline.strip().split(':')
                tlist.append(tline[0])
            useradd = input("账户名称:")
            success_1 = "成功创建用户：%s" %(useradd)
            if useradd in tlist:
                print(e_1 )
            elif useradd == "exit":
                break
            else:
                passwd = input("请输入密码：")
                length = len(passwd)
                if length == 0 :
                    print(e_2)
                elif length > 6:
                    with open('ming.txt','a')as r_3:
                        w_1 = '%s:%s:0\n' %(useradd,passwd)
                        r_3.write(w_1)
                        s_1 = success_1.center(30,'-')
                        print(s_1)
                        break
                else:
                    print(e_3)

    elif sr_1 == '2':
        flag = False
        while True:
            username = input("账户名称:")
            l = open('lock.txt','r')
            for lline in l.readlines():
                lline = lline.strip()
                if username == lline:
                    print("账号被锁")
                    flag = True
                    l.close()
                    break
            if  flag == True:
                break

            u = open('ming.txt','r')
            for uline in u.readlines():
                user,password,mony = uline.strip().split(':')

                if username == user:
                    i = 0
                    while  i < 3:
                        passwd = input('账户密码:')
                        i +=1
                        if passwd == password:
                            print('欢迎%s登陆在线购物平台' % username)
                            flag = True
                            u.close()
                            break
                        else:
                            if i >= 3:
                                with open('lock.txt','a') as l_2:
                                    l_2.write(username + '\n')
                                    l.close()
                                exit("试了太多次,将被锁定，请联系管理员")
                            print('密码输入错误，还有%d次机会' % (3 - i))
                    break
            else:
                print("用户输入错误，请重新输入")


            while True:
                print("1.购物 2.查看购物车 3.查询余额 4.充值 b.返回登陆 q.退出")
                print("------------------------------------------------")
                choice_2 = input("输入序号：")
                flag_1 = False
                while True:
                    if choice_2 == "1":
                        while True:
                            for index,g in enumerate(shopping_list):
                                print(index,g[0],g[1])
                            print("-------------------------")
                            print("c.查看购物车 b.返回 q.退出")
                            print("-------------------------")
                            choice = input("键入数字选择商品：").strip()
                            if choice.isdigit():
                                choice = int(choice)
                                p_price = shopping_list[choice][1]
                                if p_price < salary:
                                    shop_list.append(shopping_list[choice])
                                    total += p_price
                                    salary -= p_price
                                    print("-------------------------")
                                    print("您购买了%s，余额为%s"%(shopping_list[choice][0],salary))
                                    print("-------------------------")
                                else:
                                    print("-------------------------")
                                    print("您的余额不足")
                                    print("-------------------------")
                            elif choice == "c":
                                while True:
                                    print("----------购物车----------")
                                    for k,v in enumerate(shop_list):
                                        print(k,v[0],v[1])
                                    print("已消费金额为：%s"%total)
                                    print("您的可用余额：%s"%salary)
                                    print("-------------------------")
                                    print("d.删除商品 b.返回购物 q.结算退出")
                                    print("-------------------------")
                                    choice_1 = input("请键入字母选择功能：")
                                    print("-------------------------")
                                    if choice_1 == "d":
                                        print("-------------------------")
                                        print("输入数字为删除商品，输入字母b为返回购物车")
                                        print("-------------------------")
                                        while True:
                                            choice_2 = input("请选择：")
                                            if choice_2.isdigit():
                                                choice_2 = int(choice_2)
                                                d_price = shop_list[choice_2][1]
                                                shop_list.remove(shop_list[choice_2])
                                                total -= d_price
                                                salary += d_price
                                                print("-------------------------")
                                                print("商品%s删除成功，可用余额为：%s"%(shop_list[choice_2][0],salary))
                                                print("-------------------------")
                                            elif choice_2 == "b":
                                                break
                                    elif choice_1 == "b":
                                        flag = True
                                        break
                                    else:
                                        print("----------购物清单----------")
                                        for k,v in enumerate(shop_list):
                                            print(k,v[0],v[1])
                                        print("总消费金额为：%s"%total)
                                        print("您的可用余额：%s"%salary)
                                        print("--------欢迎下次再来-------")
                                        exit(0)
                            elif choice == "b":
                                break
                            elif choice == "q":
                                print("----------购物清单----------")
                                for k,v in enumerate(shop_list):
                                    print(k,v[0],v[1])
                                print("总消费金额为：%s"%total)
                                print("您的可用余额：%s"%salary)
                                print("--------欢迎下次再来--------")
                                exit(0)
                            else:
                                print("-------------------------")
                                print("您的输入有误，请重新输入")
                                print("-------------------------")
                        if flag == True:
                            break
                    elif choice_2 == "2":
                        print("----------购物车----------")
                        for k,v in enumerate(shop_list):
                            print(k,v[0],v[1])
                        print("已消费金额为：%s"%total)
                        print("您的可用余额：%s"%salary)

                        print("-------------------------")
                        break
                    elif choice_2 == "3":
                        with open('ming.txt','r')as m_1:
                            mony_1 = m_1.readlines()
                        for mline in mony_1:
                            (user,password,mony) = mline.strip().split(':')
                            print(salary)
                            flag_1 = True
                            break
                        break

                    elif choice_2 == "4":
                        z  = 0
                        while z < 1:
                            chongzhi = int(input("输入金额:"))
                            passwd_1 = input("请输入密码：")
                            m = open('ming.txt','r+')
                            m_2 = m.readlines()

                            for mline in m_2:
                                (user,password,mony) = mline.strip().split(':')

                                if passwd_1 == password:
                                    mony_2 = (chongzhi + int(mony))

                                    w_2 = '%s:%s:%s\n' %(username,password,mony_2)
                                    m.write(w_2)
                                    print("充值成功")
                                    print(mony)
                                    flag = True
                                    break
                                continue
                            break
                        if flag == True:
                            break

                    elif choice_2 == "b":
                        flag = True
                        break

                    elif choice_2 == "q":
                        exit(ex_1)
                    else:
                        print(e_4)
                        break
                    break
                if flag == True:
                    break
            break
    elif sr_1 == 'q':
        exit(ex_1)
    else:
        print(e_4)
        print('                                   ')