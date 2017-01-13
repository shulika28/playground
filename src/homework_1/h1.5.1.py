__author__ = 'Ihor'
import unittest

print('enter binary number:')
'''num1 = input()
print('enter decimal number:')
num2 = input()'''

class TestConvertMethod(unittest.TestCase):
    def test_bin_to_dec(self):
        self.assertEqual(bin_to_dec(1011110), 94, 'nifiga')


def bin_to_dec(b_num):
    b_num = str(b_num)
    d_num = 0
    for i in range(len(b_num)):
        d_num += int(b_num[i]) * \
                2 ** (len(b_num) - i - 1)
    return d_num



def dec_to_bin(d_num):
    b_num = ''
    while d_num != 1:
        b_num += str(d_num % 2)
        d_num = d_num // 2
    b_num += '1'
    return b_num[::-1]



print(bin_to_dec(1011110))
print(dec_to_bin(15))


unittest.main()