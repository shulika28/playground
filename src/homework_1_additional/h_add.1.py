__author__ = 'Ihor'
a = float(input())
b = float(input())
c = float(input())


def is_right_triangle(c1, c2, h):
    eps = 0.00001
    return c1 * c1 + c2 * c2 - h * h < eps


if is_right_triangle(a, b, c) or \
   is_right_triangle(c, b, a) or \
   is_right_triangle(b, a, c):
    print('It is right triangle')
else:
    print('It isn`t right triangle')