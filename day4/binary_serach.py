#!/usr/bin/python
# -*-coding:utf-8-*-


def binary_serach(date_source,find_n):
    mid = int(len(date_source)/2)

    if len(date_source) >=1:
        if date_source[mid] >find_n:
            print('date in left of [%s]' %date_source[mid])
            #print(date_source[:mid])
            binary_serach(date_source[:mid],find_n)
        elif date_source[mid] < find_n:
            print('date in right fo [%s]' %date_source[mid])
            #print(date_source[mid:])
            binary_serach(date_source[mid:],find_n)

        else:
            print('found find_s',date_source[mid])
    else:
        print('cannot find.....')



if __name__ == '__main__':
    data = list(range(1,600000))
    #print(data)
    binary_serach(data,1)