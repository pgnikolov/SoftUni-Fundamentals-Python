# You will receive an initial list with groceries separated by an exclamation mark "!".
# After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
# • "Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
# • "Unnecessary {item}" - remove the item with the given name, only if it exists in list. Otherwise, skip this command.
# • "Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one.
# Otherwise, skip this command.
# • "Rearrange {item}" - if the grocery exists in the list, remove it from its current position and
# add it at the end of the list. Otherwise, skip this command.

groceries = [item for item in input().split("!")]

command = input()

while command != "Go Shopping!":
    info = command.split()
    action = info[0]
    current_item = info[1]
    if action == "Urgent" and current_item not in groceries:
        groceries.insert(0, current_item)
    elif action == "Unnecessary" and current_item in groceries:
        groceries.remove(current_item)
    elif action == "Correct" and current_item in groceries:
        new_item = info[2]
        index_to_change = groceries.index(current_item)
        groceries[index_to_change] = new_item
    elif action == "Rearrange" and current_item in groceries:
        groceries.remove(current_item)
        groceries.append(current_item)

    command = input()

print(*groceries, sep=", ")
