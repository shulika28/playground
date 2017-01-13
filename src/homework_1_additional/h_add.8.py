__author__ = 'Ihor'

price = float(input('enter the price, UAH\n'))

print(0.9*price if price > 1000 else price)