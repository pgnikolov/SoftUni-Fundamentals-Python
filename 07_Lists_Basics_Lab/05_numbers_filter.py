# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
#     • even
#     • odd
#     • negative
#     • positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

lines = int(input())
list_of_numbers = []
list_of_filtered = []

for n in range(1, lines + 1):
    number = int(input())
    list_of_numbers.append(number)

command = input()

for num in list_of_numbers:
    if command == "even":
        if num % 2 == 0:
            list_of_filtered.append(num)
    elif command == "odd":
        if not num % 2 == 0:
            list_of_filtered.append(num)
    elif command == "negative":
        if num < 0:
            list_of_filtered.append(num)
    elif command == "positive":
        if num >= 0:
            list_of_filtered.append(num)
print(list_of_filtered)
