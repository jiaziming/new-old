#!/usr/bin/python
# -*-coding:utf-8-*-

# a = iter(['alex','eroc','jack'])
#
# print(a)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())


def cash_out(amount):
    while amount >0:
        amount -= 1
        yield 1
        #return 1
        print("又来取钱了")

atm= cash_out(5)

print(atm.__next__())
print(atm.__next__())
print("花掉、花掉")
print(atm.__next__())
print(atm.__next__())
