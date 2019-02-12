#!/usr/bin/python
# -*-coding:utf-8-*-

data = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]

'''
#for index,i in enumerate(data[0:-1]):
    if i >data[index+1]:
        tmp = data[index+1]
        data[index+1] = i
        data[index] = tmp

'''
for j in range(1,len(data)):
    for i in range (len(data)-j):
        if data[i] >data[i+1]:
            tmp = data[i+1]
            data [i+1] =data[i]
            data[i] = tmp
    print(data)

