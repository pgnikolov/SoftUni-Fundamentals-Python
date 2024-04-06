lines = int(input())
is_odd = False

for i in range(lines):
    num = int(input())
    if num % 2 != 0:
        print(f"{num} is odd!")
        is_odd = True
        break

if not is_odd:
    print("All numbers are even.")
