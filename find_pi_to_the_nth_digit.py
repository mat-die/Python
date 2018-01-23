# This script will take an input number n and prints PI with n digits
import math

pi = math.pi
less_than_ten = "Please choose a number less than 10..."

n = input("Give me a number...")

if int(n) > 10:
    print(less_than_ten)
else:
    format_string = '.' + n + 'f'
    print(format(pi, format_string))
