# Write a program that reads an integer n. Then, for all numbers in the range [1, n],
# print the number and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11.

# n = int(input())
#
# for i in range(1, n + 1):
#     sum_of_digits = 0
#     digits = i
#     while digits > 0:
#         sum_of_digits += digits % 10
#         digits = int(digits / 10)
#     if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
#         print(f'{i} -> True')
#     else:
#         print(f'{i} -> False')


n = int(input())
for i in range(1, n+1):
    digit_sum = sum(int(digit) for digit in str(i))
    if digit_sum in [5, 7, 11]:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
