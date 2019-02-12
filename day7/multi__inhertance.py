#!/usr/bin/python
# -*-coding:utf-8-*-


class A:
    N = 'A'
    def f2(self):
        print('form to A')

class B(A):
    N = 'B'
    def f1(self):
        print('form to B')
    #def f2(self):
    #   print('f2 form to B')
class C(A):
    N = 'C'
    def f2(self):
        print('form to C')

class D(B,C):
    ''' test '''
    pass


d =D()
d.f1()
d.f2()
print(d.__doc__)
print(d.__module__)

