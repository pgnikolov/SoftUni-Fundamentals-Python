# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list. You should remove the smallest ones,
# and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".

list_num = input().split(" ")
remove_counter = int(input())

list_int = [int(char) for char in list_num]

for i in range(1, remove_counter + 1):
    list_int.remove(min(list_int))


result = ", ".join(str(char) for char in list_int)

print(result)
