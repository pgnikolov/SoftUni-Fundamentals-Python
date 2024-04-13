# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().

nums = [int(digit) for digit in input().split()]
even_numbers = filter(lambda num: num % 2 == 0, nums)
print(list(even_numbers))
