# Receive a single number and write a function that returns the sum of all even and all odd digits in a given number.
# The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

def sum_of_even_and_odd_digits(num):
    num_as_string = str(num)
    even_sum = 0
    odd_sum = 0
    for index in range(len(num_as_string)):
        if int(num_as_string[index]) % 2 == 0:
            even_sum += int(num_as_string[index])
        else:
            odd_sum += int(num_as_string[index])
    return print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


number = int(input())
sum_of_even_and_odd_digits(number)
