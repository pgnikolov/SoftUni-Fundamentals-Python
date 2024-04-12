list_of_items = input().split("|")
budget = float(input())
item_type = []
potential_items = []
buyed_items = []
for item in list_of_items:
    item_type.append(item.split("->"))
for item in item_type:
    if item[0] == "Clothes" and float(item[1]) <= 50:
        potential_items.append(float(item[1]))
    elif item[0] == "Shoes" and float(item[1]) <= 35:
        potential_items.append(float(item[1]))
    elif item[0] == "Accessories" and float(item[1]) <= 20.50:
        potential_items.append(float(item[1]))
spended = 0
for item in potential_items:
    if item <= budget:
        budget -= item
        spended += item
        buyed_items.append(str(item))
income = 0
for price in buyed_items:
    money = float(price) * 1.40
    print(f'{money:.2f}', end=' ')
    income += money
print()
print(f'Profit: {income - spended:.2f}')
if budget + income >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
