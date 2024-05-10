# You will receive a journal with some collecting items, separated with a comma and a space (", ").
# After that, until receiving "Craft!" you will be receiving different commands split by " - ":
#     • "Collect - {item}" - you should add the given item to your inventory.
#     If the item already exists, you should skip this line.
#     • "Drop - {item}" - you should remove the item from your inventory if it exists.
#     • "Combine Items - {old_item}:{new_item}" - you should check if the old item exists.
#     If so, add the new item after the old one. Otherwise, ignore the command.
#     • "Renew – {item}" – if the given item exists, you should change its position and put it last in your inventory.

inventory_list = input().split(', ')

while True:
    command = input().split(' - ')
    if command[0] == "Craft!":
        break
    item = command[1]

    if command[0] == "Collect":
        if item not in inventory_list:
            inventory_list.append(item)
    elif command[0] == "Drop":
        if item in inventory_list:
            inventory_list.remove(item)
    elif command[0] == "Combine Items":
        old_item, new_item = command[1].split(':')
        if old_item in inventory_list:
            old_item_index = inventory_list.index(old_item)
            inventory_list.insert(old_item_index + 1, new_item)
    elif command[0] == "Renew":
        if item in inventory_list:
            inventory_list.remove(item)
            inventory_list.append(item)


print(*inventory_list, sep=", ")
