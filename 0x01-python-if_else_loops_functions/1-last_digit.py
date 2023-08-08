#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is zero")
elif (number % 10) < 6:
    if  number < 0:
        number *= -1
        print(f"Last digit of {number * (-1):d} is {(number % 10) * (-1):d} and is less than 6 and not 0")
    elif (number % 10) > 0:
        print(f"Last digit of {number:d} is {last_digit:d} and is less than 6 and not 0")
