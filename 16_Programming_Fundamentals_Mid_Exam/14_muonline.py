# initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon's rooms.
# Each room is separated with '|' (vertical bar): "room1|room2|room3…"
#     • "potion"
#         ◦ You are healed with the number in the second part. But your health cannot exceed your initial health (100).
#         ◦ First print: "You healed for {amount} hp."
#         ◦ After that, print your current health: "Current health: {health} hp."
#     • "chest"
#         ◦ You've found some bitcoins, the number in the second part.
#         ◦ Print: "You found {amount} bitcoins."
#     • In any other case, you are facing a monster, which you will fight.
#     The second part of the room contains the attack of the monster.
#     You should remove the monster's attack from your health.
#         ◦ If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
#         ◦ If you've died, print "You died! Killed by {monster}." and your quest is over.
#         Print the best room you've managed to reach: "Best room: {room}"
# "You've made it!
# Bitcoins: {bitcoins}
# Health: {health}"

health = 100
bitcoins = 0
success = True
commands = [action.split() for action in input().split("|")]
rooms = 0

for i in range(len(commands)):
    rooms += 1
    if commands[i][0] == "potion":
        if health < 100:
            if health + int(commands[i][1]) <= 100:
                health += int(commands[i][1])
                print(f"You healed for {int(commands[i][1])} hp.")
            elif health + int(commands[i][1]) > 100:
                needed_hp = 100 - health
                health = 100
                print(f"You healed for {needed_hp} hp.")
            print(f"Current health: {health} hp.")
        else:
            print(f"You healed for 0 hp.")
            print(f"Current health: {health} hp.")
    elif commands[i][0] == "chest":
        bitcoins += int(commands[i][1])
        print(f"You found {int(commands[i][1])} bitcoins.")
    else:
        monster = commands[i][0]
        attack = int(commands[i][1])
        health -= attack
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            success = False
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {rooms}")
            break

if success:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
