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
