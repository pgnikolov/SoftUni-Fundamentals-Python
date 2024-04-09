# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
#     • One with all the positive (including 0) numbers
#     • One with all the negative numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"

lines = int(input())

positive = list()
negative = list()

for n in range(lines):
    num = int(input())
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print(f"{positive}")
print(f"{negative}")
print(f"Count of positives: {len(positive)}\nSum of negatives: {sum(negative)}")
