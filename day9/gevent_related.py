#!/usr/bin/python
# -*-coding:utf-8-*-

import gevent

def foo():
    print("\033[32;1m Running in foo\033[0m")
    gevent.sleep(1)
    print("\033[32;1m Explicit context switch to foo again\033[0m")

def bar():
    print("Explicit context to bar ")
    gevent.sleep(1)
    print("Implicit context switch back to  bar")

def ex():
    print("\033[31;1m Implicit context to ex\033[0m")
    gevent.sleep(1)
    print("\033[31;1m Implicit conte xt switch to back to ex\033[0m")

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(ex),
])

