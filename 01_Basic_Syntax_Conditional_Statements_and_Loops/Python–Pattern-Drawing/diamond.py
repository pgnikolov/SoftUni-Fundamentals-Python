rows = 5

for row in list(range(1, rows + 1, 2)) + list(range(rows - 2, 0, -2)):
    spaces = " " * ((rows - row) // 2)
    stars = "*" * row
    print(spaces + stars)
