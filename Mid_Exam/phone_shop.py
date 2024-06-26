phones = input().split(', ')

while True:
    command = input()
    if command == "End":
        break
    actoins = command.split(' - ')
    if actoins[0] == "Add":
        if actoins[1] in phones:
            continue
        else:
            phones.append(actoins[1])
    elif actoins[0] == 'Remove':
        if actoins[1] in phones:
            phones.remove(actoins[1])
        else:
            continue
    elif actoins[0].startswith('Bonus'):
        old_phone, new_phone = actoins[1].split(':')
        if old_phone in phones:
            new_phone_index = phones.index(old_phone) + 1
            phones.insert(new_phone_index, new_phone)
    elif actoins[0] == 'Last':
        if actoins[1] in phones:
            phones.remove(actoins[1])
            phones.append(actoins[1])
        else:
            continue

print(', '.join(phones))
