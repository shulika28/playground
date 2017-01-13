__author__ = 'Ihor'

v_ms = float(input('enter velocity in meters per second\n'))
v_kh = float(input('enter velocity in kilometers per hour\n'))


def kh_to_ms(v):
    return v*3600/1000


eps = 0.00001
if v_ms - kh_to_ms(v_kh) < eps:
    print('velocity is the same')
elif v_ms > kh_to_ms(v_kh):
    print(str(v_ms) + ' m/s is higher')
else:
    print(str(v_kh) + ' k/h is higher')