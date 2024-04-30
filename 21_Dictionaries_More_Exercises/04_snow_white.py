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

dwarfs_dict = {}

command = input()

while not command == "Once upon a time":
    info = command.split(" <:> ")
    name = info[0]
    color = info[1]
    physics = int(info[2])
    if color not in dwarfs_dict:
        dwarfs_dict[color] = {}
        dwarfs_dict[color][name] = physics
    else:
        if name not in dwarfs_dict[color]:
            dwarfs_dict[color][name] = physics
        elif name in dwarfs_dict[color] and physics > dwarfs_dict[color][name]:
            dwarfs_dict[color][name] = physics
    command = input()

sorted_dwarfs = dict(sorted(dwarfs_dict.items(), key=lambda x: (-max(x[1].values()), -len(x[1]))))

for color, dwarfs in sorted_dwarfs.items():
    for name, physics in dwarfs.items():
        print(f"({color}) {name} <-> {physics}")

