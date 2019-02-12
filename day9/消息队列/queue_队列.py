#!/usr/bin/python
# -*-coding:utf-8-*-
import queue

q = queue.Queue(maxsize=3)


class Foo(object):
    def __init__(self,n):
        self.n = n

q.put([1,2,3])
q.put(Foo(1))
q.put(1)
#q.put(3,timeout=3)
#q.get(timeout=3)
date = q.get_nowait()
#date2 = q.get_nowait()
q.put(2)
print(date,type(date))
#print(date2,type(date2))
print(q.full())