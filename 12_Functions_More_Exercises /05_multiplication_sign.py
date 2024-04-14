# You will receive three integer numbers. Write a program that finds if their multiplication
# (the result) is negative, positive, or zero. Try to do this WITHOUT multiplying the 3 numbers.

def multiplication_sign(a, b, c):
    nums = [a, b, c]
    negative_count = sum(1 for num in nums if num < 0)
    if nums.count(0) >= 1:
        return "zero"
    elif negative_count % 2 == 0 or negative_count == 0:
        return "positive"
    else:
        return "negative"


n1 = int(input())
n2 = int(input())
n3 = int(input())
print(multiplication_sign(n1, n2, n3))
