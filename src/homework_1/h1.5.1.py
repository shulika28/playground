__author__ = 'Ihor'

print 'enter binary number:'
num1 = input()
print 'enter decimal number:'
num2 = input()

def bin_to_dec(b_num):
    b_num = str(b_num)
    d_num = 0
    try:
        for i in range(len(b_num)):
            d_num += int(b_num[i])*2**(len(b_num) - i - 1)
        return d_num
    except:
        return False

def dec_to_bin(d_num):
    b_num = ''
    try:
        while d_num != 1:
            b_num += str(d_num % 2)
            d_num /= 2
        b_num += '1'
        return b_num[::-1]
    except:
        return False

print bin_to_dec(num1)
print dec_to_bin(num2)




