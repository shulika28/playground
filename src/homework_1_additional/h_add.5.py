__author__ = 'Ihor'

num1 = float(input())
num2 = float(input())
num3 = float(input())

nums = [num1, num2, num3]
eps = 0.000001

print(abs(nums[0] - nums[1]) < eps or abs(nums[0] - nums[2]) < eps or abs(nums[2] - nums[1]) < eps)