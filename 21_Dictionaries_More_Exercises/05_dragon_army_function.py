def dragon_stats(dragon_input):
    # dragon info assign values and check for missing to replace them with default
    type, name, dmg, hp, armor = dragon_input.split()
    if dmg == "null":
        dmg = 45
    if hp == "null":
        hp = 250
    if armor == "null":
        armor = 10
    return type, name, int(dmg), int(hp), int(armor)


amount_dragons = int(input())
dragon_dict = {}

for dragon in range(amount_dragons):
    dragon_info = input()
    type, name, dmg, health, armor = dragon_stats(dragon_info)

    if type not in dragon_dict.keys():
        dragon_dict[type] = {}
    if name not in dragon_dict[type].keys():
        dragon_dict[type][name] = 0
    dragon_dict[type][name] = [dmg, health, armor]

for dragon_type in dragon_dict:
    dragon_names_sorted = sorted(dragon_dict[dragon_type].keys())

    avr_dmg, avr_hp, avr_armor = 0, 0, 0
    avr_len = len(dragon_dict[dragon_type].keys())
    for stats in dragon_dict[dragon_type].values():
        avr_dmg += stats[0]
        avr_hp += stats[1]
        avr_armor += stats[2]
    avr_dmg = avr_dmg/avr_len
    avr_hp = avr_hp/avr_len
    avr_armor = avr_armor/avr_len

    print(f"{dragon_type}::({avr_dmg:.2f}/{avr_hp:.2f}/{avr_armor:.2f})")

    [print(f"-{dragon_name} ->"
           f" damage: {dragon_dict[dragon_type][dragon_name][0]},"
           f" health: {dragon_dict[dragon_type][dragon_name][1]},"
           f" armor: {dragon_dict[dragon_type][dragon_name][2]}")
     for dragon_name in dragon_names_sorted]