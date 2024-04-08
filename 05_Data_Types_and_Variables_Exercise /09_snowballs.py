# You will receive N – an integer, the number of snowballs
# On the following lines, you will receive 3 inputs for each snowball:
#     • The weight of the snowball (integer).
#     • The time needed for the snowball to get to its target (integer).
#     • The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.
# Input
#     • On the first input line, you will receive N – the number of snowballs.
#     • On the next N*3 input lines, you will be receiving data about each snowball.
# Constraints
#     • The number of snowballs (N) will be an integer in the range [0, 100].
#     • The weight is an integer in the range [0, 1000].
#     • The time is an integer in the range [1, 500].
#     • The quality is an integer in the range [0, 100].

n = int(input())
higest_value = 0
hv_time = 0
hv_weight = 0
hv_quality = 0

for ball in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > higest_value:
        higest_value = value
        hv_time = time
        hv_weight = weight
        hv_quality = quality

print(f"{hv_weight} : {hv_time} = {higest_value:.0f} ({hv_quality})")

