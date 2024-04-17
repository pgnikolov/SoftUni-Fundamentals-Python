# You will be receiving to-do notes until you get the command "End".
# The notes will be in the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).

to_do_list = [0] * 10

while True:
    command = input()
    if command == "End":
        break
    actions = command.split("-")
    priority = int(actions[0])
    note = actions[1]
    to_do_list.pop(priority)
    to_do_list.insert(priority, note)

if command == "End":
    result = [char for char in to_do_list if char != 0]
    print(result)
