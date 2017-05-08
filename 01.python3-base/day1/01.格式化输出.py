#!/usr/bin/env python
#coding:utf8
#Author:Felix zheng
# Function: 格式化输出

name = input("name:")
age = int(input("age:")) # integer 转换为整型
# 查看变量类型 print(type(age))
job = input("job:")
salary = int(input("salary:"))

info = '''
------- info of %s -------
Name:%s
Age:%d
Job:%s
Salary:%d
''' %(name,name,age,job,salary)

print (info)

info2 = '''
------- info2 of {_name} -------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
''' .format(_name=name,
            _age=age,
            _job=job,
            _salary=salary)

print (info2)

info3 = '''
------- info3 of {0} -------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
''' .format(name,age,job,salary)

print (info3)
