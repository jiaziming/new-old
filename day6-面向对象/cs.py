#!/usr/bin/python
# -*-coding:utf-8-*-


class Role(object):

    def __init__(self,name,role,weapon,life_value):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value


    def buy_weapon(self,weapon):

        print("%s is buying [%s]" %(self.name,self.weapon))
        #self.weapon = weapon


#Role 的实例
#把一个抽象的类  变成一个具体的对象  过程叫实例化
p1 = Role("alex","Police","B51",100)
p2 = Role("jack","Terrorist","B46",100)

p1.buy_weapon("AK47")   #Role.buy_weapon('p1','Ak47')
p2.buy_weapon("B31")

Role.ac = "Janpanese Brand"



print("p1:",p1)
print("p2:",p2.weapon)