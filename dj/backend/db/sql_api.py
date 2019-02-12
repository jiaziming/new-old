#!/usr/bin/python
# -*-coding:utf-8-*-

import sys,os

#print(sys.path)
base_dir = (os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

sys.path.append(base_dir)



from config import settings

def db_auth(configs):
    if configs.database["user"] == 'root' and configs.database["password"] == '123':
        print("db authentication passed!")
        return True
    else:
        print("db login error .....")


def select(table,column):

    if db_auth(settings):


        if table == "user":
            user_info = {
                "001":["alex",22,"negineer"],
                "002":["erice",23, "chef"],
                "003":["jack", 43, "baoan"],
            }

            return user_info
