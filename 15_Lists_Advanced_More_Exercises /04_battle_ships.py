# You will be given a number n representing the number of rows of the field. On the following n lines,
# you will receive each field row as a string with numbers separated by a space.
# Each number greater than zero represents a ship with health equal to the number value.
# After that, you will receive the squares that are being attacked in the format:
# "{row}-{col} {row}-{col}". Each time a square is being attacked, if there is a ship (number greater than 0),
# you should reduce its value by 1. If a ship's health reaches zero, it is destroyed.
# After the attacks have ended, print how many ships were destroyed.

total_ships_destroyed = 0
battlefield = []
battlefield_rows = int(input())

for row in range(battlefield_rows):
    battlefield.append(input().split(" "))

attack_zones = input().split(" ")

for zone in attack_zones:
    row, col = zone.split("-")
    row = int(row)
    col = int(col)
    if int(battlefield[row][col]) > 0:
        battlefield[row][col] = str((int(battlefield[row][col]) - 1))
        if battlefield[row][col] == "0":
            total_ships_destroyed += 1

print(total_ships_destroyed)
