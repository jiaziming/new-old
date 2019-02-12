#!/usr/bin/python
# -*-coding:utf-8-*-

import threading,time

data = []
def run(n):
    time.sleep(3)
    data.append(n**n)
    print("from child")



res_list =[]
for i in range(10):
    t = threading.Thread(target=run,args=[i,])
    t.start()
    res_list.append(t)

for i in res_list:
    i.join()

print('-------',data)