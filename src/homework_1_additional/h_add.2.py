__author__ = 'Ihor'
num1 = float(input())
num2 = float(input())
num3 = float(input())

nums = [num1, num2, num3]

for el in nums:
    print(el ** 3 if el > 0 else 0)