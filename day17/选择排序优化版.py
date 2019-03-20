#!/usr/bin/python
# -*-coding:utf-8-*-

import random

def selection_sort(array):
    for i in range(len(array)):
        smallest_index = i
        for j in range(i,len(array)):
            if array[smallest_index] > array[j]:
                smallest_index = j

        tmp = array[i]
        array[i] = array[smallest_index]
        array[smallest_index] = tmp



if __name__ == '__main__':
    array =[] #[476, 387, 245, 76, 139, 202, 90, 331, 609, 260, 758, 28, 74, 423, 463, 977, 563, 849, 937, 844]


    for i in range(5000):
        array.append(random.randrange(100000))
    print(array)

    selection_sort(array)
    print(array)
