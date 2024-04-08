# Write a program, which sums the ASCII codes of N characters and prints the sum.
# On the first line, you receive N – number of lines. On the following N lines – you will receive a letter per line.
# Print the total sum in the following format: "The sum equals: {total_sum}".

n = int(input())

total_sum = 0

for i in range(n):
    letter = input()
    for char in letter:
        total_sum += ord(char)

print(f"The sum equals: {total_sum}")
