city_gird = [int(el) for el in input().split("|")]
robot_items = 0

while True:
    command = input()
    if command == "Adventure over":
        break
    actions = command.split('$')
    if actions[0] == 'Step Backward':
        starting_cell = int(actions[1])
        steps = int(actions[2])
        if 0 <= starting_cell < len(city_gird):
            position = (starting_cell - steps) % len(city_gird)
            robot_items += city_gird[position]
            city_gird[position] = 0
    elif actions[0] == "Step Forward":
        starting_cell = int(actions[1])
        steps = int(actions[2])
        if 0 <= starting_cell < len(city_gird):
            position = (starting_cell + steps) % len(city_gird)
            robot_items += city_gird[position]
            city_gird[position] = 0
    elif actions[0].startswith("Double"):
        info = actions[0].split()
        value_index = int(info[1])
        if 0 <= value_index < len(city_gird):
            city_gird[value_index] *= 2
    elif actions[0] == 'Switch':
        city_gird.reverse()

print(" - ".join(map(str, city_gird)))
print(f"Robo finished the adventure with {robot_items} items!")
