#!/usr/bin/python
# -*-coding:utf-8-*-
import random


'''
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[j-1] > array[j]:
                tmp = array[j-1]
                array[j-i] = array[j]
                array[j] = tm
'''

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i,):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp



if __name__ == "__main__":
    array = [476, 387, 245, 76, 139, 202, 90, 331, 609, 260, 758, 28, 74, 423, 463, 977, 563, 849, 937, 844]

    # for i in range(20):
    #      array.append(random.random(1,20))

    print(array)

    bubble_sort(array)
    print(array)




