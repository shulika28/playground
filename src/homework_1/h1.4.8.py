__author__ = 'Ihor'

num1 = int(input())
num2 = int(input())


def last_num(num):
    return num % 10


print(last_num(num1) == last_num(num2))

'case with ternary operator:'
print(True if last_num(num1) == last_num(num2) else False)