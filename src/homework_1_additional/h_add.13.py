__author__ = 'Ihor'
from functools import reduce

a = float(input())
b = float(input())
c = float(input())


def general_task(a, b, c):
    nums = [a, b, c]
    names = ['a', 'b', 'c']
    output = list(map(lambda x: x * 2, nums)) if reduce((lambda x, y: x + y), nums) > 0 else list(
        map(lambda x: 0, nums))
    for i in range(len(names)):
        print(names[i], '=', output[i])


def task(a, b, c):
    if a + b + c > 0:
        a *= 2
        b *= 2
        c *= 2
    else:
        a = 0
        b = 0
        c = 0
    print('a =', a)
    print('b =', b)
    print('c =', c)


general_task(a, b, c)
task(a, b, c)
