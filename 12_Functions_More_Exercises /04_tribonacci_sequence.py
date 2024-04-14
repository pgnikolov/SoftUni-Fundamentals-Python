def tribonacci_rec(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return tribonacci_rec(n - 1) + tribonacci_rec(n - 2) + tribonacci_rec(n - 3)


def tribonacci(n):
    result = []
    for i in range(0, n):
        result.append(str(tribonacci_rec(i)))
    return result


num = int(input())
print(" ".join(tribonacci(num)))
