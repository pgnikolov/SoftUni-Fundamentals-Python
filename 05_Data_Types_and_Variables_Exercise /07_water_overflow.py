# You have a water tank with a capacity of 255 liters.
# On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive liters of water (integers), which you should pour into your tank.
# If the capacity is not enough, print "Insufficient capacity!" and continue to the next line.
# On the last line, print the liters in the tank.

capacity = 255
n = int(input())
filled_water = 0

for i in range(n):
    liters = int(input())
    if liters > capacity:
        print("Insufficient capacity!")
    else:
        filled_water += liters
        capacity -= liters

print(filled_water)
