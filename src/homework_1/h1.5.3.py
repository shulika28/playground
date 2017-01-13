__author__ = 'Ihor'

num = input()


def counter_eights(num):
    return len(list(filter(lambda x: x == '8', str(num))))


print(counter_eights(num))

