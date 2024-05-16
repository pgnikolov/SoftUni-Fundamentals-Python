def num_def(number):
    if num == 0:
        return "zero"
    else:
        sign = "positive" if number > 0 else "negative"
        size = "large" if abs(number) > 1000000 else ("small" if abs(number) < 1 else "")
    return f"{size} {sign}"


num = float(input())

print(num_def(num))
