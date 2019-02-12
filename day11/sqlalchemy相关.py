#!/usr/bin/python
# -*-coding:utf-8-*-

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

user = Table('user',metadata,
            Column('id',Integer,primary_key=True),
            Column('name',String(20)),
)

color = Table('color',metadata,
            Column('id',Integer,primary_key=True),
            Column('name',String(29)),
)

enine = create_engine("mysql+pymysql://root:jia@123@localhost:3306/test",max_overflow= 5)

'''
#插入数据 增
conn =enine.connect()
sql = user.insert().values(name="alex")
conn.execute(sql)
conn.close()
'''

'''
#删除数据 删  

conn =enine.connect()
sql = user.delete().where(user.c.name == 'wu')
'''

'''

'''
conn =enine.connect()


sql = user.select([user, ])
sql = user.select([user.c.id, ])
sql = user.select([user.c.name, color.c.name]).where(user.c.id==color.c.id)
sql = user.select([user.c.name]).order_by(user.c.name)
sql = user.select([user]).group_by(user.c.name)
conn.execute(sql)

metadata.create_all(enine)