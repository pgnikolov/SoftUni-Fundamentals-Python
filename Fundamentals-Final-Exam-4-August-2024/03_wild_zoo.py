zoo_data = {"Areas": {}}


def add_animal(details):
    animal, food_needed, area = details.split("-")
    zoo_data[animal] = zoo_data.get(animal, 0) + int(food_needed)
    if area not in zoo_data["Areas"]:
        zoo_data["Areas"][area] = []
    if animal not in zoo_data["Areas"][area]:
        zoo_data["Areas"][area].append(animal)


def feed_animal(details):
    animal, food_given = details.split("-")
    if animal in zoo_data:
        zoo_data[animal] -= int(food_given)
        if zoo_data[animal] <= 0:
            del zoo_data[animal]
            for area_animals in zoo_data["Areas"].values():
                if animal in area_animals:
                    area_animals.remove(animal)
                    break
            print(f"{animal} was successfully fed")


command_input = input()

while command_input != "EndDay":
    action, info = command_input.split(": ")
    if action == "Add":
        add_animal(info)
    elif action == "Feed":
        feed_animal(info)
    command_input = input()

if zoo_data:
    print("Animals:")
    for animal_name, food_quantity in zoo_data.items():
        if animal_name != "Areas":
            print(f" {animal_name} -> {food_quantity}g")

if zoo_data["Areas"]:
    print("Areas with hungry animals:")
    for area_name in zoo_data["Areas"]:
        if zoo_data["Areas"][area_name]:
            print(f" {area_name}: {len(zoo_data['Areas'][area_name])}")
