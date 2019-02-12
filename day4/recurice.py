#!/usr/bin/python
# -*-coding:utf-8-*-

#
# def calc(n):
#     print(n)
#     if n /2 >1:
#         res = calc(n/2)
#         #return calc(n/2)
#         print("res:",res)
#     print('N:',n)
#     return n
# calc(100)


#斐波那契

def func(arg1,arg2,stop):
    if arg1 == 0:
        print(arg1,arg2)
    arg3 = arg1 + arg2
    print(arg3)
    if arg3< stop:
        func(arg2,arg3,stop)

func(0,1,30)