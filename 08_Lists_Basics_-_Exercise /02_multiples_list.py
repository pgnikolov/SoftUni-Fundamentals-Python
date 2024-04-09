# Write a program that receives two numbers (factor and count).
# It creates a list with a length of the given count that contains only integer numbers,multiples of the given factor.
# The numbers should be only positive, they should be arranged in ascending order, starting from value of the factor.

factor = int(input())
count = int(input())

number = list()

for num in range(1, count +1):
    number.append(factor * num)

print(number)
