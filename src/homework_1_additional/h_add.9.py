__author__ = 'Ihor'

height = float(input('enter your height\n'))
weight = float(input('enter your weight\n'))


def perfect_weight(height):
    return height - 100


print('your perfect weight is', perfect_weight(height))

print('your weight is perfect')if perfect_weight(height) == weight \
    else print('you have to eat ' + ('less','more')[weight < perfect_weight(height)])