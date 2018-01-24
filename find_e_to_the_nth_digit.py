"""
This script will take an input number n and prints e with n digits
The number has to be smaller than or equal to 10
"""
import math

e = math.e

less_than_ten = "Please choose a number less than 10..."

n = input("Give me a number...")

if int(n) > 10:
    print(less_than_ten)
else:
    format_string = '.' + n + 'f'
    print(format(e, format_string))
