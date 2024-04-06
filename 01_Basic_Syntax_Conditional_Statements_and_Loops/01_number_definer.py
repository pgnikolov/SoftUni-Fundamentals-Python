# Write a program that reads a floating-point number and:
#     • prints "zero" if the number is zero
#     • prints "positive" or "negative"
#     • adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds
# 1 000 000

num = float(input())

if num == 0:
    print("zero")
elif 0.00 < num < 1.00:
    print("small positive")
elif -1.00 < num < 0.00:
    print("small negative")
elif 1.00 <= num <= 1000000:
    print("positive")
elif num > 1000000:
    print("large positive")
elif -1000000 <= num <= -1.00:
    print("negative")
elif num < -1000000:
    print("large negative")
