#!/usr/bin/python
# -*-coding:utf-8-*-

import re


#(pattern,date_source)
# 规则        数据源

m = re.match('ab','abasdqwe12easd')
#print(m.group())
m = re.match('[0-9]','1asdnio12a')
m = re.match('[0-9]{0,15}','12893ndmao12')
m = re.match('[0-9]{10}','12893ndmao12')
m = re.findall('[0-9]{1,10}','12893ndmao12')
m = re.findall('[a-zA-Z]{1,10}','12893ndmao12')
m = re.findall(".*",'12893ndmao12')
m = re.findall(".+",'12893ndmao12')


if m:
    print(m)