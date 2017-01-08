__author__ = 'Ihor'

num1 = input()
num2 = input()
nums = [num1, num2]

if max(nums) % min(nums) == 0:
    print True
else:
    print False
print '\n' + 'integral part:' + str(int(max(nums)/min(nums))) + ', modulo:' + str(max(nums) % min(nums))