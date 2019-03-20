#!/usr/bin/python
# -*-coding:utf-8-*-

import random,time

def quick_sort(array):
    k = array[0]
    left_flag = 0
    right_flag = len(array) -1

    while array[right_flag] >k :    #代表要继续往左边移动
        right_flag -= 1

    tmp = array[left_flag]
    array[left_flag] = array[right_flag]


    #左边的小旗子开始向右移动
    tmp = array[left_flag]
    array[left_flag] = array[right_flag]
    array[right_flag] = tmp
    print(array)

    #开始把问题分半
    quick_sort(array,0,left_flag)







if __name__ == '__main__':

    array = [476, 387, 245, 76, 139, 202, 90, 331, 609, 260, 758, 28, 74, 423, 463, 977, 563, 849, 937, 844]
    print(array)
    time_start = time.time()

    quick_sort(array)
    print(time_start)
    print(array)