# divisor = int(input())
# boundary = int(input())
#
# for i in range(boundary, divisor, -1):
#     if i % divisor == 0:
#         print(i)
#         break

divisor = int(input())
boundary = int(input())

largest_multiple = (boundary // divisor) * divisor
print(largest_multiple)
