__author__ = 'Ihor'

num = str(input())

if len(num) == 3:
    if num[0] == num[1] and num[0] == num [2]:
       print ('All figures in the numder are the same')
    elif num[0] == num[1] or num[0] == num [2] or num[1] == num [2]:
       print('There are the same figures in the number')
    else:
        print('There are no the same figures in the number')
else:
    print('entered number is not three digit')