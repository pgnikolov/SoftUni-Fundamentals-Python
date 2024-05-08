# Write a program to read a sequence of integers and find and print the
# top 5 numbers greater than the average value in the sequence, sorted in descending order.
# Input
#     • Read from the console a single line holding space-separated integers.
# Output
#     • Print the above-described numbers on a single line, space-separated.
#     • If less than 5 numbers hold the property mentioned above, print less than 5 numbers.
#     • Print "No" if no numbers hold the above property.

nums = [int(char) for char in input().split()]

average_value = sum(nums) / len(nums)

greater_than_avr = [num for num in nums if num > average_value]
sort_greats = sorted(greater_than_avr, reverse=True)

if not greater_than_avr:
    print("No")
elif len(sort_greats) <= 5:
    sort_greats_str = [str(char) for char in sort_greats]
    print(" ".join(sort_greats_str))
elif len(sort_greats) > 5:
    top5 = [str(char) for char in sort_greats[:5]]
    print(" ".join(top5))
