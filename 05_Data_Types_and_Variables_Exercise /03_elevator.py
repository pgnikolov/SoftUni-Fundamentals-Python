# Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.

n = int(input())
p = int(input())
#
# if n <= p:
#     print("1")
# elif n > p and n % p == 0:
#     print(n // p)
# else:
#     print(n // p + 1)

import math

courses = math.ceil(n / p)
print(courses)
