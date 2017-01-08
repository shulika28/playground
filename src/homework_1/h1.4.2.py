__author__ = 'Ihor'

n1 = input()
n2 = input()
n3 = input()

if n1 > n2:
    max = n1
    min = n2
else:
    max = n2
    min = n1

if n3 > max:
    max = n3
elif n3 < min:
    min = n3
print 'max:' + str(max)
print 'min:' + str(min)