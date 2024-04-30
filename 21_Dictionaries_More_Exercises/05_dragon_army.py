# There may be missing stats in the input, though. If a stat is missing you should assign it default values.
# Default values are as follows: health 250, damage 45, and armor 10. Missing stat will be marked as "null".
# The input is in the following format "{type} {name} {damage} {health} {armor}".
# The "type" and the "name" are strings. The "damage", the "health", and the "armor" are integers.
# Any of the integers may be assigned a "null" value.
# Input
#     • On the first line, you are given the number N -> the number of dragons to follow.
#     • On the next N lines, you are given input in the above-described format.
#     There will be a single space separating each element.
# Output
#     • Print the aggregated data on the console.
#     • For each type, print the average stats of its dragons in the format
# "{type}::({damage}/{health}/{armor})".
#     • Damage, health, and armor should be rounded to two digits after the decimal separator.
#     • For each dragon, print its stats in the format "-{Name} -> damage: {damage}, health: {health}, armor: {armor}".

amount_of_dragons = int(input())
dragon_types = {}


for _ in range(amount_of_dragons):
    info = input().split()

    # format {type} {name} {damage} {health} {armor}.

    dragon_type = info[0]
    name = info[1]
    damage = 45
    if not info[2] == "null":
        damage = int(info[2])
    health = 250
    if not info[3] == "null":
        health = int(info[3])
    armor = 10
    if not info[4] == "null":
        armor = int(info[4])

    if dragon_type not in dragon_types:
        dragon_types[dragon_type] = {}
    if name not in dragon_types[dragon_type]:
        dragon_types[dragon_type][name] = {}
    dragon_types[dragon_type][name] = {'damage': damage, 'health': health, 'armor': armor}

for dragon_type, dragon in dragon_types.items():
    stats = dragon.values()
    dmg = 0
    hlth = 0
    arm = 0
    for drag in stats:
        dmg += drag['damage']
        hlth += drag['health']
        arm += drag['armor']
    print(f"{dragon_type}::({dmg / len(stats) :.2f}/{hlth / len(stats) :.2f}/{arm / len(stats) :.2f})")
    for key, value in sorted(dragon.items()):
        print(f"-{key} -> damage: {value['damage']}, health: {value['health']}, armor: {value['armor']}")
