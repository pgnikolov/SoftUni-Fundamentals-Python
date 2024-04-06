num_in_range = False


while not num_in_range:
    num = float(input())
    if 1 <= num <= 100:
        num_in_range = True
        print(f"The number {num} is between 1 and 100")
        break

