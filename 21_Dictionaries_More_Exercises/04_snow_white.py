# You will be receiving several input lines which contain data about each dwarf in the following format:
# {dwarf_name} <:> {dwarf_hat_color} <:> {dwarf_physics}
# The "dwarf_name" and the "dwarf_hat_color" are strings. The "dwarf_physics" is an integer.
# You must store the data about the dwarfs in your program. There are several rules though:
#     • If 2 dwarfs have the same name but different colors, they should be considered different dwarfs,
#     and you should store them both.
#     • If 2 dwarfs have the same name and the same color, store the one with the higher physics.
# When you receive the command "Once upon a time", the input ends. You must order the dwarfs by physics in descending
# order and then by the total count of dwarfs with the same hat color in descending order.
# Then you must print them all.
# Input
#     • The input will consist of several input lines, containing dwarf data in the format, specified above.
#     • The input ends when you receive the command "Once upon a time".
# Output
#     • As output, you must print the dwarfs, ordered in the way, specified above.
#     • The output format is: "({hat_color}) {name} <-> {physics}"

dwarfs = {}
hat_colors = {}

command = input()

while not command == "Once upon a time":
    info = command.split(" <:> ")
    name = info[0]
    hat_color = info[1]
    if hat_color not in hat_colors:
        hat_colors[hat_color] = 0
    hat_colors[hat_color] += 1
    physics = int(info[2])
    name_color = name + hat_color
    if name_color not in dwarfs:
        # dwarfs[name_plus_color] = {}
        dwarfs[name_color] = {'name': name, 'color': hat_color, 'physics': physics}
    else:
        if physics > dwarfs[name_color]["physics"]:
            dwarfs[name_color]["physics"] = physics
            hat_colors[hat_color] -= 1
    command = input()

current_dwarfs = list(dwarfs.values())

for dwarf in current_dwarfs:
    for color in hat_colors:
        if color == dwarf["color"]:
            # var. for counting dwarfs with equal colors
            dwarf["samecolor"] = hat_colors[color]

sorted_current_dwarfs = sorted(current_dwarfs, key=lambda x: (-x["physics"], -x["samecolor"]))

for el in sorted_current_dwarfs:
    print(f"({el['color']}) {el['name']} <-> {el['physics']}")
