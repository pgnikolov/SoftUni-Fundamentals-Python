# Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros,
# and moves them to the back without messing up the other elements. Print the resulting integer list.

nums = [int(num) for num in input().split(", ")]
nulls = nums.count(0)
null_list = [0] * nulls
num_no_null = [num for num in nums if not num == 0]
final_nums = num_no_null + null_list
print(final_nums)
