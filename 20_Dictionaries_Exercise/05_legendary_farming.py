# possible items are:
#     • "Shadowmourne" - requires 250 Shards
#     • "Valanyr" - requires 250 Fragments
#     • "Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race. At that point,
# you have to print that the corresponding legendary item is obtained.
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.
# Input
# Each line comes in the following format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"

key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
junk = {}

materials = input().lower().split(" ")

end_game = False


while not end_game:
    for i in range(0, len(materials) - 1, 2):
        if not end_game:
            amount = int(materials[i])
            material = materials[i + 1]
            if material in key_materials:
                key_materials[material] += amount
                if key_materials[material] >= 250:
                    key_materials[material] -= 250
                    end_game = True
                    print(f"{legendary_items[material]} obtained!")
            else:
                if material not in junk:
                    junk[material] = 0
                junk[material] += amount
    if not end_game:
        materials = input().lower().split(" ")

for k, v in key_materials.items():
    print(f"{k}: {v}")

for k, v in junk.items():
    print(f"{k}: {v}")
