#!/usr/bin/python
# -*-coding:utf-8-*-

import time,threading

def run(n):
    print('(%s) -------runing -----\n' %n)
    time.sleep(2)
    print('----done----')


def main():
    for i in range(5):
        a = threading.Thread(target=run,args=[i,])
        a.start()
        #a.join()
        print('starting thread',a.getName())

m =threading.Thread(target=main,args=[])
m.setDaemon(True)
m.start()
m.join(timeout=2)
print('------main thread done------')