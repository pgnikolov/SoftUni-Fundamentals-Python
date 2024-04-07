# You will be given an integer that represents a distance in meters.
# Write a program that converts meters to kilometers formatted to the second decimal point.

distance = int(input())

km = distance / 1000

print(f"{km:.2f}")
