shop = {}
total_sold = 0

while True:
    info = input()
    command = info.split()
    if command[0] == "Complete":
        break
    elif command[0] == "Receive":
        if command[2] in shop:
            shop[command[2]] = shop[command[2]] + int(command[1])
        else:
            shop[command[2]] = int(command[1])
    elif command[0] == "Sell":
        if command[2] not in shop:
            print(f"You do not have any {command[2]}.")
            continue
        if shop[command[2]] >= int(command[1]):
            total_sold += int(command[1])
            shop[command[2]] -= int(command[1])
            print(f"You sold {int(command[1])} {command[2]}.")
        elif shop[command[2]] < int(command[1]):
            total_sold += shop[command[2]]
            print(f"There aren't enough {command[2]}. You sold the last {shop[command[2]]} of them.")
            shop[command[2]] = 0


if shop:
    for key, value in shop.items():
        if value > 0:
            print(f"{key}: {value}")

print(f"All sold: {total_sold} goods")
