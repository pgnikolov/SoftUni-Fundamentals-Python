amount_heros = int(input())
heros = {}
for i in range(amount_heros):
    name, hp, mp = input().split()
    heros[name] = {'hitpoints': int(hp), 'manapoints': int(mp)}

while True:
    command = input()
    if command == 'End':
        break
    info = command.split(' - ')

    if info[0] == 'CastSpell':
        hero_name, mp_needed, spell_name = info[1], int(info[2]), info[3]
        if heros[hero_name]['manapoints'] >= mp_needed:
            heros[hero_name]['manapoints'] -= mp_needed
            print(f'{hero_name} has successfully cast {spell_name} and now has {heros[hero_name]["manapoints"]} MP!')
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif info[0] == 'TakeDamage':
        hero_name, damage, attacker = info[1], int(info[2]), info[3]
        heros[hero_name]['hitpoints'] -= damage
        if heros[hero_name]['hitpoints'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heros[hero_name]['hitpoints']} HP left!")
        else:
            heros.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    elif info[0] == 'Recharge':
        hero_name, recharge_qnt = info[1], int(info[2])
        if heros[hero_name]['manapoints'] + recharge_qnt > 200:
            needed_recharge = 200 - heros[hero_name]['manapoints']
            heros[hero_name]['manapoints'] = 200
            print(f"{hero_name} recharged for {needed_recharge} MP!")
        else:
            heros[hero_name]['manapoints'] += recharge_qnt
            print(f"{hero_name} recharged for {recharge_qnt} MP!")
    elif info[0] == 'Heal':
        hero_name, heal_qnt = info[1], int(info[2])
        if heros[hero_name]['hitpoints'] + heal_qnt > 100:
            needed_heal = 100 - heros[hero_name]['hitpoints']
            heros[hero_name]['hitpoints'] = 100
            print(f"{hero_name} healed for {needed_heal} HP!")
        else:
            heros[hero_name]['hitpoints'] += heal_qnt
            print(f"{hero_name} healed for {heal_qnt} HP!")

for hero in heros:
    print(f"{hero}\n"
          f"    HP: {heros[hero]['hitpoints']}\n"
          f"    MP: {heros[hero]['manapoints']}")
