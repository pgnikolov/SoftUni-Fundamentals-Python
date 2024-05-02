num_of_electrons = int(input())
remaining_electrons = num_of_electrons
electron_list = []
level = 1
electron_for_level = 2 * level ** 2
while remaining_electrons > electron_for_level:
    remaining_electrons -= electron_for_level
    electron_list.append(electron_for_level)
    level += 1
    electron_for_level = 2 * level ** 2
else:
    electron_list.append(remaining_electrons)

print(electron_list)
