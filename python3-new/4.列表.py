#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2017/7/13 22:54
# @File    : 4列表.py
# @Author  : Felix-zh
# @E-mail  : chengfeng56@qq.com
# @Function: 列表
'''
列表包含以下函数：
1.cmp(list1,list2):比较两个列表的元素
2.len(list):列表元素的个数
3.max(list):返回列表元素最大值
4.min(list):返回列表元素最小值
5.list(seq):将元组转换为列表
#######
列表包含以下方法：
1.list.append(obj):在列表末尾添加新的对象
2.list.count(obj):统计某个元素在列表出现的次数
3.list.extend(seq):在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4.list.index(obj):从列表中找出某个值第一个匹配的索引位置
5.list.insert(index.obj):将对象插入列表
6.list.pop(obj=list[-1]):移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7.list.remove(obj):移除列表中某个值的第一个匹配项
8.list.reverse():反向列表中的元素
9.list.sort([func]):队员列表进行排序
'''
#print("python中的编码，在文件最开始部分添加 # -*- coding: utf-8 -*- 设置编码")
#print("python中的换行，在行的末尾添加\n \\n的标识")

# 创建列表 list
number_list = [1, 3, 5, 7, 9]

print("number list: " + str(number_list))

string_list = ["abc", "bbc", "pyton"]

mixed_list = ["python", "java", 3, 12]

#print("string_list: " +str(string_list))
#print("mxied_list: " + str(mxied_list))
# 取列表内的值
second_num = number_list[1]
third_string = string_list[2]
fourth_mixed =mixed_list[3]

print("second_num: {0} third_string: {1} fourth_mixed: {2}".format(second_num, third_string, fourth_mixed))

# 更新列表number_list 1的值
number_list[1] = 30
print("number_list after: " + str(number_list))

# 删除列表内的值
del number_list[1]
print("number_list after del: " + str(number_list))

print(len([1,2,3])) # 列表内参数个数
print([1,2,3] + [4,5,6]) # 多个列表相加
print(['hello'] * 4) # 一个列表重复多次
print(3 in [1,2,3]) # 检查值是否在一个列表内

# 列表截取
abcd_list = ['a', 'b', 'c', 'd']
print(abcd_list[1])
print(abcd_list[-2]) # 从右边截取
print(abcd_list[1:])
print(abcd_list[:2])