#!/usr/bin/python
# -*-coding:utf-8-*-


class school_member(object):
    member_number = 0

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enrool()


    def enrool(self):
        school_member.member_number += 1
        print("\033[32;11mthe [%s] school member [%s] is enrool!\033[0m" %(self.member_number,self.name))


    def tell(self):
        print("my name is %s" %self.name)

class techer(school_member):
    def __init__(self,name,age,sex,cource,salary):
        super(techer,self).__init__(name,age,sex)
        #school_member.__i __(self.name,age,sex)
        self.cource = cource
        self.salary = salary

    def teching(self):
        print("teacher [%s] is teching [%s]" %(self.name,self.cource))


class student(school_member):
    def __init__(self,name,age,sex,courcse,tuition):
        super(student,self).__init__(name,age,sex)
        self.course = courcse
        self.tuition = tuition

    def pay_tution(self):
        print("ca ,student [%s] payint tution [%s]" %(self.name,self.tuition))

t1 = techer('alex',23,'F','py',10000)
t2 = techer('jack',2213,'N/A','py',100001)

s1 = student('sanjiang',213,'F','py',12)
s2 = student('error',123,'F','py',12123)

t1.tell()
s1.tell()

t1.teching()
s1.pay_tution()