__author__ = 'Ihor'

weekday = float(input('enter weekday\n'))
call_duration = float(input('enter call duration\n'))


def call_price(weekday, duration):
    if weekday < 1 or weekday > 7:
        return 'Error: Number of weekdays must be in range from 1 to 7'
    minute_price = 5
    weekend_minute_price = minute_price * 0.8
    return (minute_price * duration, weekend_minute_price * duration) \
        [weekday == 6 or weekday == 7]


print(call_price(weekday, call_duration))
