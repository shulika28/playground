__author__ = 'Ihor'
# coding:utf8

num = int(input())

right_form = {0: 'копійок', 1: 'копійка', 2: 'копійки', 3: 'копійки', 4: 'копійки'}
for i in range(5,20):
    right_form[i] = 'копійок'

print(num, right_form[num] if num < 20 else right_form[num % 10])
