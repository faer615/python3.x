#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Felix_zh
#E-mail:chengfeng56@qq.com
#Function: 操作SQLite3

import sqlite3                        # 引入SQLite3包模块
conn = sqlite3.connect('test.db')     # 打开数据库文件 test.db

# 获取游标对象
cur = conn.cursor()

# 执行一系列的SLQ语句
# 建立一个表
cur.execute("create table if not exists demo(num int,str varchar(20));")
# 插入一些记录
cur.execute("insert into demo values(%d, '%s')" %(1,'aaa'))
cur.execute("insert into demo values(%d, '%s')" %(2,'bbb'))
cur.execute("insert into demo values(%d, '%s')" %(3,'ccc'))

# 更新一条记录
cur.execute("update demo set str='%s' where num = %d" %('ddd',3))

# 查询
cur.execute("select * from demo;")
rows = cur.fetchall()
print("number of records: ", len(rows))
for i in rows:
    print(i)

# 提交事务
conn.commit()

# 关闭游标对象
cur.close()

# 关闭数据库连接
conn.close()