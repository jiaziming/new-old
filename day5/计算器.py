#!/usr/bin/python
# -*-coding:utf-8-*-

import re

def calc(formula):
    parenthese_flag =True
    while parenthese_flag :
        m = re.search("\([^()]+\)",formula)
        if m :
            print(m.group())
        break



if __name__ == "__main__":
    formula = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
    res = calc(formula)