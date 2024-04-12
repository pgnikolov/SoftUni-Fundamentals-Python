# Write a program that rounds all the given numbers, separated by a single space,
# and prints the result as a list. Use round().
nums = [round(float(char)) for char in input().split(" ")]
print(nums)
