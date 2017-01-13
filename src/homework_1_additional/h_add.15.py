__author__ = 'Ihor'
import math

cirlce_area = float(input('enter area of a cirlce\n'))
square_area = float(input('enter area of a square\n'))


def is_square_in_cirlce(c_ar, s_ar):
    c_diam = 2 * (c_ar / math.pi) ** (1/2)
    s_diag = (2 * s_ar) ** (1/2)
    return s_diag <= c_diam


def is_cirlce_in_square(c_ar, s_ar):
    c_diam = 2 * (c_ar / math.pi) ** (1/2)
    s_side = s_ar ** (1/2)
    return c_diam <= s_side


print('square is inside circle' if is_square_in_cirlce(cirlce_area,square_area) else 'square is outside circle')
print('circle is inside square' if is_cirlce_in_square(cirlce_area,square_area) else 'circle is outside square')