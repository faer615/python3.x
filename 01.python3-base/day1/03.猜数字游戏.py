#!/usr/bin/env python
#coding:utf8
#Author:Felix zheng
#Function: 猜数字游戏

age_of_felix = 32
count = 0
for i in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == age_of_felix:
        print("yes,you got it.")
        break
    elif guess_age < age_of_felix:
        print("think smaller!")
    else:
        print("think bigger!")

    count +=1
else:
    print("you have tried too many times... shutdown")