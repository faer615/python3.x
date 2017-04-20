#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh

data = {
    '北京':{
        "东城":{
            "王府井":["购物","美食"],"灯市口":["休闲","娱乐"]
        },
        "西城":{
            "西单":["大悦城","购物"],"故宫":["皇城","紫禁城"]
        },
        "朝阳":{
            "团结湖":["闹市区","电影院"],"呼家楼":["闲逛","遛弯"]
        },
    },
    '山东':{
        "济南":{
            "历城区":["火车站","趵突泉"],"市中区":["区政府","八一桥"]
        },
        "青岛":{
            "市北区":["博物馆","山东路"],"市南区":["青岛大学","广电大厦"]
        },
        "淄博":{
            "张店区":["市政府","淄博站"],"临淄区":["牛山路","齐都花园"]
        },
    },
}

while True:
    for i in data:
        print(i)

    choice = input("选择进入1>>：")
    if choice in data:
        while True:
            for i2 in data[choice]:
                print("\t",i2)
            choice2 = input("选择进入2>>：")
            if choice2 in data[choice]:
                while True:
                    for i3 in data[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("选择进入3>>：")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t",i4)
                        choice4 = input("最后一层，按b返回>>：")
                        if choice4 == "b":
                            pass
                    if choice3 == "b":
                        break
            if choice2 == "b":
                break