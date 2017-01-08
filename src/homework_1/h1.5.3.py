__author__ = 'Ihor'
import math

num = input()

def counter_eights(num):
    count = 0
    for el in str(num):
        if el == '8':
            count +=1
    return count

print counter_eights(num)