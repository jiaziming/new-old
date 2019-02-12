#!/usr/bin/python
# -*-coding:utf-8-*-

import  re

string = '192.168.2.233333'     #ip地址匹配

m =re.match("([0-9]{1,3}\.){3}\d{1,3}" ,string)

print(m.group())