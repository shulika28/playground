__author__ = 'Ihor'

month_num = int(input('enter the number of month\n'))


def what_season(month_num):
    if month_num == 1 or month_num == 2 or month_num == 12:
        return 'Winter'
    elif month_num == 3 or month_num == 4 or month_num == 5:
        return 'Spring'
    elif month_num == 6 or month_num == 7 or month_num == 8:
        return 'Summer'
    elif month_num == 9 or month_num == 10 or month_num == 11:
        return 'Autumn'
    else:
        return 'Error. The number of month must be in the range from 1 to 12'


print (what_season(month_num))