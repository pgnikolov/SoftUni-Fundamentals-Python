def add_food(addition: list, store: dict):
    if addition[1] in store:
        store[addition[1]] = store[addition[1]] + int(addition[2])
    else:
        store[addition[1]] = int(addition[2])

    return store


def sell_food(sold: list, store: dict, sold_amount: int):
    if store[sold[1]] >= int(sold[2]):
        sold_amount += int(sold[2])
        store[sold[1]] -= int(sold[2])
        print(f"You sold {int(sold[2])} {sold[1]}.")
    elif store[sold[1]] < int(sold[2]):
        sold_amount += store[sold[1]]
        print(f"There aren't enough {sold[1]}. You sold the last {store[sold[1]]} of them.")
        store[sold[1]] = 0

    return store, sold_amount


shop = {}
total_sold = 0

while True:
    command = input().split()
    if command[0] == "Complete":
        break
    elif command[0] == "Recieve":
        shop = add_food(command, shop)
    elif command[0] == "Sell":
        shop, total_sold = sell_food(command, shop, total_sold)


if shop:
    for key, value in shop.items():
        print(f"{key}: {value}")

print(f"All sold: {total_sold}")
