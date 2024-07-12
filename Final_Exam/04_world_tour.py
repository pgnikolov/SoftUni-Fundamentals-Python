destination = input()

while True:

    command = input()
    if command == 'Travel':
        break
    info = command.split(":")

    if info[0] == "Add Stop":
        if int(info[1]) <= len(destination):
            destination = destination[:int(info[1])] + info[2] + destination[int(info[1]):]
        else:
            pass
    elif info[0] == "Remove Stop":
        if int(info[1]) <= len(destination) and int(info[2]) + 1 <= len(destination):
            destination = destination[:int(info[1])] + destination[int(info[2]) + 1:]
        else:
            pass
    elif info[0] == "Switch":
        if info[1] in destination:
            destination = destination.replace(info[1], info[2])
        else:
            pass
    print(destination)

print(f"Ready for world tour! Planned stops: {destination}")
