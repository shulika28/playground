__author__ = 'Ihor'

num1 = int(input())


def is_lucky(num):
    num = str(num)
    sum1 = num[0] + num[1] + num[2]
    sum2 = num[3] + num[4] + num[5]
    return sum1 == sum2


print('number is lucky' if is_lucky(num1) else 'number is ordinary')
