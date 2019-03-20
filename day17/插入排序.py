#!/usr/bin/python
# -*-coding:utf-8-*-

import  random,time

def insertion_sort(array):
    for i in range(1,len(array)):
        position = i
        current_val = array[i]

        while position >0 and current_val < array[position-1]:
            array[position] = array[position -1]
            position -= 1

        array[position] = current_val

if __name__ == '__main__':

    array = [92, 77, 67, 8, 6, 84, 55, 85, 43, 67]

    time_stast = time.time()
    insertion_sort(array)
    print(time_stast)
    print(array)

