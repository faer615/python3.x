#!/usr/bin/env python
#coding: utf8
#Author: Felix
#E-mail: chengfeng56@qq.com
#Function: 购物车优化版

product_list =[
    ['Mi 5s',1999],
    ['HaWei Mate8',2799],
    ['IPhone 6s plus',6888],
    ['ThinkPad T460P',7888],
    ['MacBook Air 13',6988],
    ['MacBook Pro 13',9288],
]

shopping_list = [] # 定义空列表
salary = input("Input your salary：") # 输入工资
if salary.isdigit(): # 判断是不是数字
    salary = int(salary) # 是数字转换成 int
    while True: # 进入循环
        for index,item in enumerate(product_list): # 建立商品索引给列表加下标
            print(index,item) # 打印索引及商品列表
        #break
        '''方法2 enumerate 取列表下标
        for item in shopping_list:
            print(shopping_list.index(item),item)
        break
        '''
        user_choice = input("选择要购买的商品：") # 选择购买商品
        if user_choice.isdigit(): # 判断用户输入数字类型
            user_choice = int(user_choice) # 转换成int类型
            if user_choice < len(product_list) and user_choice >=0: # 判断用户输入是否在范围内
                p_itme =product_list[user_choice] # 通过下标，添加购买商品列表
                if p_itme[1] <= salary: # 判断工资是否够用
                    shopping_list.append(p_itme) # 添加到已购买商品列表
                    salary -= p_itme[1] # 扣除费用
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_itme,salary)) # 显示已购买的商品和费用
                else:
                    print("\033[41;1m你的余额只剩[%s]了，买不起了。\033[0m" % salary) # 显示余额
            else:
                print("product code [%s] is not exist!" % user_choice) # 提示商品不存在
        elif user_choice == 'q': # 输入 q 退出
            print('----------shopping list----------') # 打印购买商品
            for p in shopping_list:
                print(p) # 打印商品
            print("Your current balance:",salary) # 显示余额
            exit()
        else:
            print("invalid option")