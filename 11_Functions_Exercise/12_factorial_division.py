# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

import math

a = int(input())
b = int(input())

print(f'{math.factorial(a) / math.factorial(b):.2f}')
