__author__ = 'Ihor'
import math

num = input()


def factorial(num):
    mult = 1
    for multer in range(num):
        mult *= multer + 1
    return mult


def factorial_stirl(num):
    return int((2 * math.pi * num) ** 0.5 * (num / math.exp(1)) ** num)


print (factorial(num))
print (factorial_stirl(num))
