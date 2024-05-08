targets = [int(char) for char in input().split()]
command = input()

while command != "End":
    actions = command.split()
    action = actions[0]
    index = int(actions[1])
    value = int(actions[2])
    if action == "Shoot":
        if index in range(len(command)):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif action == "Add":
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print('Invalid placement!')
    elif action == "Strike":
        if index in range(value, len(targets) - value):
            del targets[index - value: index + value + 1]
        else:
            print('Strike missed!')
    command = input()

print(*targets, sep="|")
