#!/usr/bin/python
# -*-coding:utf-8-*-


class animal(object):

    count = 10
    def __init__(self,name):
        self.name = name
        self.num = None

    hobbie = 'meat'

    @classmethod        #类方法 不能访问实例变量
    def talk(self):
        print('%s is talking ....' % self.hobbie )

    @staticmethod       #静态方法 不能访问类变量和实例变量
    def walk(self):
        print('%s is walking .....' % self.hobbie)
    @property           #把方法变成属性  已让可以访问类变量和实例变量

    def habit(self):
        print('%s habit is xxoo ' %self.name)


    @property
    def total_players(self):
        return self.num

    @total_players.setter
    def total_players(self,num):
        return self.num
        print('total players:',self.num)

    @total_players.deleter
    def total_players(self,num):
        return self.num
        print('total players:',self.num)



#animal.hobbie
#animal.talk()
a = animal('alex')
a.talk()
print(a.total_players)
a.total_players = 3
del a.total_players
print(a.total_players)

a.habit