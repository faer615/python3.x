#!/usr/bin/env python
#coding:utf8
#Author:Felix zheng

age_of_felix = 32
count = 0
while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_felix:
        print("yes,you got it.")
        break
    elif guess_age < age_of_felix:
        print("think smaller!")
    else:
        print("think bigger!")
    count +=1
    if count == 3:
        countine_comfirm = input("Do you want to keep guessing ...? ")
        if countine_comfirm != 'n':
            count = 0
#else:
#    print("you have tried too many times... fuck off")