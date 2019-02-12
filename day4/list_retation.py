#!/usr/bin/python
# -*-coding:utf-8-*-

date = [[col for col in range(4)] for now in range(4)]

'''
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
-------------
[0, 0, 0, 0]
[1, 1, 1, 1]
[2, 2, 2, 2]
[3, 3, 3, 3]

'''




for now in date:
    print(now)


print('--------------')

for r_index,now in enumerate(date):
    #print(row)
    for c_index in range(r_index,len(now)):
        tmp = date[c_index][r_index]
        date[c_index][r_index] = now[c_index]
        date[r_index][c_index] = tmp

    print('--------------')

    for r in date:print(r)


