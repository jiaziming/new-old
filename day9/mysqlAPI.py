#!/usr/bin/python
# -*-coding:utf-8-*-

import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='jia@123', db='test')

cur = conn.cursor()

#reCount = cur.execute('insert into student(name,age,sex,tel,nal) values(%s,%s,%s,%s,%s)', ('place', 19,'man','1231234124','china'))    #数据库插入
#reCount = cur.execute('insert into student(name,age,sex,tel,nal) values(%s,%s,%s,%s,%s)', ('Rachel', 23,'F','1231234124','china'))

# reCount = cur.execute('insert into UserInfo(Name,Address) values(%(id)s, %(name)s)',{'id':12345,'name':'wupeiqi'})

reCount = cur.execute('select * from student')  #数据库查询


res = cur.fetchone()        #fetchone  返回一条  fetchall 返回所有   fetchmany(3)  返回指定几条
print(res)

conn.commit()
cur.close()
conn.close()

print(reCount)