#!/usr/bin/python
# -*-coding:utf-8-*-


while True:
    num1 = input('num1:')
    num2 = input('num2:')
    a = range(10)
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        a[11]

    except ValueError as e:
        print('value error:',e)

    except IndexError as e:
        print('index error:',e)

    except Exception as e:
        print('出现异常，信息如下：')
        print(e)


