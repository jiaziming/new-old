#!/usr/bin/python
# -*-coding:utf-8-*-

from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, 'hello'])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p2 = Process(target=f,args=(q,))
    p.start()
    p2.start()
    print('form parent:',q.get(),'form paren2:',q.get())  # prints "[42, None, 'hello']"

    p.join()