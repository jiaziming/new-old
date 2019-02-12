#!/usr/bin/python
# -*-coding:utf-8-*-

#from backend.db import sql_api
from backend.db.sql_api import select


def home():
    print("welcome to home page")
    q_data = select("user","dddd")
    print("query res:",q_data)

def movie():
    print("welcome to movie page")

def tv():
    print("welcome to tv page")