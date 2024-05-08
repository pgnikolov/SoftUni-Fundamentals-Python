# quantity of food, hay, and cover, which Merry buys for a month (30 days).
# On the fourth line, you will receive the guinea pig's weight.
# Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet
# , then gives it a certain amount of hay equal to 5% of the rest of the food.
# On every third day, Merry puts Puppy cover with a quantity of 1/3 of its weight.
# Calculate whether the quantity of food, hay, and cover, will be enough for a month.
# If Merry runs out of food, hay, or cover, stop the program!
# Input
#     • On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0].
#     • On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0].
#     • On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0].
#     • On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0].
# • If the food, the hay, and the cover are enough, print:
# ◦ "Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."
# • If one of the things is not enough, print:
# ◦ "Merry must go to the pet store!"

food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
pig_weight = float(input()) * 1000

food_in_stock = True

if food / 30 <= 0:
    food_in_stock = False
    print("Merry must go to the pet store!")
else:
    for day in range(1, 31):
        food -= 300
        if day % 2 == 0:
            hay -= food * 0.05
        if day % 3 == 0:
            cover -= (pig_weight / 3)
        if food <= 0 or hay <= 0 or cover <= 0:
            print("Merry must go to the pet store!")
            food_in_stock = False
            break

if food_in_stock:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
