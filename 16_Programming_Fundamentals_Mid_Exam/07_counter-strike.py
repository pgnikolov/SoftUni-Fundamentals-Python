# Write a program that keeps track of every won battle against an enemy. You will receive initial energy.
# Afterward, you will start receiving the distance you need to reach an enemy until the "End of battle"
# command is given, or you run out of energy.
# The energy you need for reaching an enemy is equal to the distance you receive. Each time you reach an enemy,
# you win a battle, and your energy is reduced. Otherwise, if you don't have enough energy to reach an enemy,
# end the program and print: "Not enough energy! Game ends with {count} won battles and {energy} energy".
# Every third won battle increases your energy with the value of your current count of won battles.
# Upon receiving the "End of battle" command, print the count of won battles in the following format:
# "Won battles: {count}. Energy left: {energy}"

energy = int(input())

refill_counter = 0
wins_counter = 0

command = input()

while command != "End of battle":
    distance = int(command)
    if energy >= distance:
        energy -= distance
        wins_counter += 1
        refill_counter += 1
        if refill_counter == 3:
            energy += wins_counter
            refill_counter = 0
    elif energy < distance:
        print(f"Not enough energy! Game ends with {wins_counter} won battles and {energy} energy")
        break
    command = input()

if command == "End of battle":
    print(f"Won battles: {wins_counter}. Energy left: {energy}")
