#!/usr/bin/python
# -*-coding:utf-8-*-

class Animal(object):
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        print('%s: 喵喵喵!' % self.name)


class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' % self.name)

'''
animals = [Cat("小青"),
           Dog("小雷")]


for animals in animals:
    print(animals.name + ':' + animals.talk())

'''



def func(obj):  # 一个接口，多种形态
    obj.talk()


c1 = Cat('小晴')
d1 = Dog('李磊')

func(c1)
func(d1)

