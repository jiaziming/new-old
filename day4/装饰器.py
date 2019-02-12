#!/usr/bin/python
# -*-coding:utf-8-*-

'''

def login(func):    #func=tv
    def inner(*args,**kwargs):
        print('passed user verification.....')
        func(*args,**kwargs)  #tv

    return inner

def home(name):
    print('welcome [%s] to home page' %name)

@login
#tv= login(tv)
def tv(name):
    print('welcome [%s] to Tv page' %name )

def moive(name,password):
    print('welcome [%s] to moive  page' %name )

#
#tv = login(tv)
tv('alex')
#moive('erice',123)

'''





def login(func):  #func=sayhi
    def weapper():
        print('login......')
        return func()   #sayhi()

    return weapper


#@login  #sayhi=longin(sayhi)
def sayhi():
    print('hello......')
    return 9


sayhi = login(sayhi)
s = sayhi()
print(s)