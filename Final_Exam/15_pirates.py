city_population_dict = {}
city_gold_dict = {}

while True:
    city_info = input()
    if city_info == "Sail":
        break
    city, population, gold = city_info.split("||")
    population, gold = int(population), int(gold)

    if city in city_population_dict:
        city_population_dict[city] += population
        city_gold_dict[city] += gold
    else:
        city_population_dict[city] = population
        city_gold_dict[city] = gold

while True:
    event_info = input().split("=>")
    event = event_info[0]

    if event == "End":
        break

    town = event_info[1]

    if event == "Plunder":
        people = int(event_info[2])
        gold = int(event_info[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        city_population_dict[town] -= people
        city_gold_dict[town] -= gold

        if city_population_dict[town] <= 0 or city_gold_dict[town] <= 0:
            city_population_dict.pop(town)
            city_gold_dict.pop(town)
            print(f"{town} has been wiped off the map!")

    elif event == "Prosper":
        gold = int(event_info[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            city_gold_dict[town] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {city_gold_dict[town]} gold.")

if city_population_dict:
    print(f"Ahoy, Captain! There are {len(city_population_dict)} wealthy settlements to go to:")
    for city, population in city_population_dict.items():
        gold = city_gold_dict[city]
        print(f"{city} -> Population: {population} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
