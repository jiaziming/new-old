#!/usr/bin/python
# -*-coding:utf-8-*-


import queue,threading,time

q = queue.Queue()


def consumer(n):
    while True:
        print("\033[32;1m consumer [%s]\033[0m get task: %s" % (n,q.get()))
        time.sleep(1)
        q.task_done()      #通知队列


def producer(n):
    count =1
    while True:
        time.sleep(1)
        if q.qsize() <3:
            print("prodeer [%s] produced a new task : %s" %(n,count))
            q.put(count)
            count += 1
            q.join()
            print('all taks has been cosumed by consumers.....')

c1 =threading.Thread(target=consumer,args=[1,])
c2 =threading.Thread(target=consumer,args=[2,])
c3 =threading.Thread(target=consumer,args=[3,])

p1 =threading.Thread(target=producer,args=['z1'])
p2 =threading.Thread(target=producer,args=['z2'])
p3 =threading.Thread(target=producer,args=['z3'])
p4 =threading.Thread(target=producer,args=['z4'])
p5 =threading.Thread(target=producer,args=['z5'])

c1.start()
c2.start()
c3.start()

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()