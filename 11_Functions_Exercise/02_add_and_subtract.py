# You will receive three integer numbers.
# Write functions named:
#     • sum_numbers() that returns the sum of the first two integers
#     • subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.

def sum_numbers(num1, num2):
    sum_nums = num1 + num2
    return sum_nums


def subtract(result, num3):
    return result - num3


def add_and_subtract(num1, num2, num3):
    result = sum_numbers(num1, num2)
    return subtract(result, num3)


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))
