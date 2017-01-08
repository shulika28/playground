__author__ = 'Ihor'

num1 = input()
num2 = input()

def last_num(num):
    return num % 10

if last_num(num1) == last_num(num2):
    print True
else:
    print False
