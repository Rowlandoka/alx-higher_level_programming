#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    last_digit = int(str(number)[-1]) * -1
else:
    last_digit = int(str(number)[-1])
first = "Last digit of "
last = " and is less than 6 and not 0"

if (last_digit > 5):
    print(first + "{} is {} and is greater than 5".format(number, last_digit))
elif (last_digit == 0):
    print(first + "{} is {} and is 0".format(number, last_digit))
else:
    print(first + "{} is {}".format(number, last_digit) + last)
