#!/usr/bin/python
# -*-coding:utf-8-*-

from multiprocessing import Process
import time

def a (name):
    time.sleep(2)
    print('Hello',name)


if __name__ == '__main__':
    p = Process(target=a,args=('alex',))
    p1 = Process(target=a,args=('error',))
    p2 = Process(target=a,args=('jack',))

    p.start()
    p1.start()
    p2.start()
    p.join()