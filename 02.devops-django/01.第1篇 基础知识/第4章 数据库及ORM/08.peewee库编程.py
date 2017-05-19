#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: peewee库编程 2.7

# 定义数据库表到Python ORM类的映射关系，连接数据库并进行CRUD等操作

# 引入peewee包的所有内容
from peewee import *

# 建立一个SQLite数据库引擎对象，该引擎打开数据库文件sampleDB.db
db = SqliteDatabase("sampleDB.db")

# 定义一个ORM的基类，在基类中指定本ORM所使用的数据库，这样在之后所有的子类就不要重复声明数据库了。
class BaseModel(Model):
    class Meta:
        database = db

# 定义course表，继承自BaseModel
class Course(BaseModel):
    id = PrimaryKeyField()
    title = CharField()
    period = IntegerField()
    description = CharField()

    class Meta:
        order_by = ('title',)
        db_table = 'course'  # 定义数据库表名

## 定义teacher表，继承自BaseModel
#class Teacher(BaseModel):
#    id = PrimaryKeyField()
#    name = CharField()
#    gender = BooleanField()
#    address = CharField()
#    course_id = ForeignKeyField(Course, to_field="id", related_name="course")
#
#    class Meta:
#        order_by = ('name')
#        db_table = 'teacher'