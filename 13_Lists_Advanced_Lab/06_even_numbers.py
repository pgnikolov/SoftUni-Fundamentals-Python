# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.

numbers = [int(n) for n in input().split(", ")]

even_index = map(lambda x: x if numbers[x] % 2 == 0 else 'no', range(len(numbers)))

even_num_index = list(filter(lambda a: a != 'no', even_index))

print(even_num_index)
