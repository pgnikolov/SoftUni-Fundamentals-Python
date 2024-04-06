# If the wolf is the closest animal to you, print "Please go away and stop eating my sheep"
# Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" N is the sheep's position in the queue.
# Note: there will always be exactly one wolf on the list.
queue = input()
animals = queue.split(", ")

# check if the last animal is wolf
if animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    sheep_in_danger = animals[0]
    sheep_position = len(animals) - 1 - animals.index("wolf")
    print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")
