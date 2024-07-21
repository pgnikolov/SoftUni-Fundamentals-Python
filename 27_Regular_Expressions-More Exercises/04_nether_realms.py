import re


def calculate_health(symbols):
    health = sum(ord(symbol) for symbol in symbols)
    return health


def calculate_damage(numbers):
    damage = sum(float(num) for num in numbers)
    return damage


def adjust_damage(damage, multipliers):
    multiplier_effect = multipliers.count("*") - multipliers.count("/")
    if multiplier_effect > 0:
        damage *= 2 ** multiplier_effect
    return damage

hp_pattern = r"[^0-9\+\-\*\/\.]"

damage_pattern = r"([\+\-]?[\d]+[.]?[\d]*)"
multiplier_pattern = r"([\*\/])"
demon_names = sorted(demon.strip() for demon in input().split(","))
for demon in demon_names:
    hp_symbols = re.findall(hp_pattern, demon)
    dmg_numbers = re.findall(damage_pattern, demon)
    multipliers = re.findall(multiplier_pattern, demon)

    demon_health = calculate_health(hp_symbols)
    demon_damage = calculate_damage(dmg_numbers)
    demon_damage = adjust_damage(demon_damage, multipliers)

    print(f"{demon} - {demon_health} health, {demon_damage:.2f} damage")
