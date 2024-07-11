n = int(input())

for _ in range(n):
    text = input()
    name = text[text.index("@") + 1:text.index("|")]
    age = text[text.index("#") + 1:text.index("*")]
    print(f"{name} is {age} years old.")
