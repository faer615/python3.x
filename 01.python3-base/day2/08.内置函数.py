#!/usr/bin/env python
#coding: utf8
#Author: Felix
#E-mail: chengfeng56@qq.com
#Function: 内置函数

name = "my \tname is {name} and i am {year} old"

print(name.capitalize()) # 首字母大写
print(name.count("z")) # 统计字符个数
print(name.center(50,"-")) # 字符居中，不足50个字符用-号补齐
print(name.expandtabs(tabsize=20)) # 将tab转换成20个空格
print(name.endswith("com")) # 判断以com结尾
print(name.find("name")) # 字符串位置
print(name[name.find("name"):]) # 字符串切片
print(name.format(name='felix',year=31)) # 01.格式化输出
print(name.format_map({'name':'felix','year':35})) # 字典格式化
print('abc123'.isalnum()) # 阿拉巴数字 + 阿拉巴字符
print('Aab'.isalpha()) # 纯英文字符
print('16'.isdecimal()) # 判定16进制
print('23'.isdigit()) #判断是否为整数
print('aB_1'.isidentifier()) # 是不是合法的标识符
print('bc'.islower()) # 是不是小写
print('AABB'.isupper()) # 是不是大写
print('332'.isnumeric()) # 是不是纯整数
print(' '.isspace()) # 是不是空格
print('My Name'.istitle()) # 是不是标题
print('+'.join(['1','2','3','4','5'])) # 转换为字符串,拼接
print(name.ljust(50,"-")) # 在右侧不足50个字符用-号补齐
print(name.rjust(50,'-')) # 在左侧不足50个字符用-号补齐
print('Felix'.lower()) #字符串全小写
print('Felix'.upper()) #字符串全大写
print('\nFelix'.lstrip()) # 去掉左边回车
print('Felix\n'.rstrip()) # 去掉右边回车
print('  Felix\n'.strip()) # 去掉回车 常用
print('Felix zh'.replace('F','f',1)) # 字符替换
print('felix zh'.rfind('z')) # 包含z的下标
print('felix zh'.split()) # 按照空格转换成列表
print('1+2\n+3+4'.splitlines()) # 根据换行符形成列表
print('Felix Zh'.swapcase()) # 大小写转换
print('felix zh'.title()) # 转换成标题
print('felix'.zfill(50)) #不足50位的使用0从左填充