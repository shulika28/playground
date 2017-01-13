__author__ = 'Ihor'
# coding:utf8

num = float(input('Яка швидкість вітру?\n'))

if num >= 1 and num < 5:
    print('слабкий')
elif num >= 5 and num < 10:
    print('помірний')
elif num >= 10 and num < 19:
    print('сильний')
elif num >= 19:
    print('ураганний')
else:
    print('немає інформації')
