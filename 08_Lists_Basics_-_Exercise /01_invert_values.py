# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

single_string = input()
string_list = single_string.split(" ")
list_nums = [int(char) for char in string_list]

for i in range(len(list_nums)):
    if list_nums[i] > 0:
        list_nums[i] = -list_nums[i]
    elif list_nums[i] < 0:
        list_nums[i] = abs(list_nums[i])

print(list_nums)

# Solution 2
#
# list_with_numbers = input().split()
# opposite_numbers = []
#
# for number in list_with_numbers:
#     opposite_number = -int(number)
#     opposite_numbers.append(opposite_number)
# print(opposite_numbers)
