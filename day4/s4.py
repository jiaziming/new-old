#!/usr/bin/python
# -*-coding:utf-8-*-


#一个参数
# def show(arg):
#     print(arg)
#
# show('1111')
#


#两个参数
# def show(arg,alex):
#
#     print(arg,alex)
#
# show('111','xxxx')

#默认参数   必须放在最后
# def show(a1,a2=999,a3=2333,a4=444):
#     print(a1,a2,a3,a4)
#
# show(111)

#指定参数
# def show(a1,a2):
#     print(a1,a2)
#
# show(a2=111,a1=222)



# def show(arg):
#     print(arg)
#
# n = [1,2,4,5]
# show(n)


# 动态参数  *args 将参数修改为元组
# def show(*args):
#     print(args)
#
# show(1,2,4,54,65,)

# *kwargs 将参数修改为字典
# def show(**kwargs):
#     print(kwargs)
#
# show(n1=88,m2=22)

# def show(*args,**kwargs):
#     print(args,type(args))
#     print(kwargs,type(kwargs))
#
# show(1,2,3,4,5, n1=22,n2=33)
#
# (1, 2, 3, 4, 5) <class 'tuple'>
# {'n2': 33, 'n1': 22} <class 'dict'>


# 字符串的格式化
# 一
# s1 = "{0} is {1}"
# r = s1.format('alex','sb')
# print(r)
#
# 二
# s1 = "{0} is {1}"
# l1 =['alex','sb']
#
# re = s1.format(*l1)
# print(re)


# s1 = "{name} is {acter}"lin
# re = s1.format(name='alex',acter='sb')
# print(re)
#
# s1 = "{name} is {acter}"
# l2 = {'name':'alex','acter':'sb'}
# re = s1.format(**l2)
# print(re)

#
# def func(a):
#     a += 1
#     return a
#
# re = func(4)
# print(a)


#lamdba 表达式
#
# func = lambda a :a +1

#
# class foo:
#
#     def __repr__(self):
#         return "bbasdasdbbbb"
#
#
# f =foo()
# ret = ascii(f)
# print(ret)
#
# a =bytes('贾子明',encoding='utf-8')
# print(a)
#
# li = ['alex','eric','jack']
#
# for i,item in enumerate(li,1):
#     print(i,item)


# a = open("jiaziming.txt",'r',encoding="utf-8")
# print(a.tell())
# a.read(2)
# print(a.tell())
#
# a.close()
#

def w1(func):   #func=f1
    def inner(arg):
        # 验证1
        # 验证2
        # 验证3
        return func(arg)
    return inner

@w1
#w1=w1(f1)
def f1(arg):
    print(f1)

f1()
