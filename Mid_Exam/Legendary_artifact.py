DESERT_COST = 15
MOUNTAIN_COST = 10
FOREST_BONUS = 7

energy = float(input())
artifact = 0
mountain = 0
artifact_found = False

while not artifact_found:
    terrain = input()
    if terrain == "Journey ends here!" or energy <= 0:
        break
    elif terrain == 'mountain':
        energy -= MOUNTAIN_COST
        mountain += 1
        if mountain == 3:
            artifact += 1
            mountain = 0
    elif terrain == 'desert':
        energy -= DESERT_COST
    elif terrain == 'forest':
        energy += FOREST_BONUS

    if artifact == 3:
        artifact_found = True
        break

if artifact_found:
    print(f"The character reached the legendary artifact with {energy:.2f} energy left.")
elif energy <= 0:
    print("The character is too exhausted to carry on with the journey.")
else:
    print(f"The character could not find all the pieces and needs {3 - artifact} more to "
          f"complete the legendary artifact.")
