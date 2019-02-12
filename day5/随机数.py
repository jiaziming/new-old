#!/usr/bin/python
# -*-coding:utf-8-*-

import random

'''
纯数据 随机数
check_code = ""

for i in range(4):
    current = random.randint(0,9)
    #check_code += str(current)
    check_code = check_code + str(current)

print(check_code)

'''

check_code = ""

for i in range(4):
    current = random.randint(0,4)
    if current != i:
        tmp = chr(random.randint(65,95))
    else:
        tmp = random.randint(0,9)

    check_code += str(tmp)

print(check_code)


