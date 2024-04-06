n = int(input())

for _ in range(n):
    letters = input()
    if "," in letters[::-1] or "." in letters[::-1] or "_" in letters[::-1]:
        print(f"{letters} is not pure!")
    else:
        print(f"{letters} is pure.")
