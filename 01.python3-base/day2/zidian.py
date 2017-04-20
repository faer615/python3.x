#!/usr/bin/env python
# coding: utf8
# Author:Felix_zh

info = {
    'stud001':"Li Qiang",
    'stud002':"Wang Lei",
    'stud003':"Xue Ming"
}

print(info)
info["stud001"]="李强" # 修改字典
info["stud004"]="陈倩" # 添加字典
#del 删除字典内容
del info["stud001"]
info.pop("stud002")
print(info.get('stud003'))
print('stud003' in info)
print(info)