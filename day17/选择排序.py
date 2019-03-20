#!/usr/bin/python
# -*-coding:utf-8-*-

def selection_sort(array):
    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[i] > array[j]:
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp




if __name__ == '__main__':
    array =[476, 387, 245, 76, 139, 202, 90, 331, 609, 260, 758, 28, 74, 423, 463, 977, 563, 849, 937, 844]

    print(array)

    selection_sort(array)
    print(array)
