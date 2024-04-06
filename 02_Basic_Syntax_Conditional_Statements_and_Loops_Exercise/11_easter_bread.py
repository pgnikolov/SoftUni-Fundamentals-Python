# Create a program that calculates how many loaves you can make (according to the recipe) with the budget you have.
# recipe for one loaf:
# Eggs 1 pack
# Flour 1 kg
# Milk 0.250 l
# The price for 1 pack of eggs is 75% of the price for 1 kg flour
# The price for 1L milk is 25% more than the price for 1 kg flour.
# Start cooking the loaves and keep making them until you have enough budget.
# For every loaf of bread that you make, you will receive 3 colored eggs
# For every 3rd bread you make, you will lose some of  colored eggs after receiving the usual 3  eggs for your bread.
# The eggs you will lose calculated when subtract 2 from your current count of loaves - ({current_bread_count} - 2)
# In the end, print the loaves of bread you made, the eggs you have collected, and the money you have left,
# formatted to the 2nd decimal place, in the following format:


budget = float(input())
flour_price_1kg = float(input())
eggs_price_1pack = flour_price_1kg * 0.75
milk_price_1l = flour_price_1kg * 1.25
price_per_loaf = eggs_price_1pack + flour_price_1kg + milk_price_1l / 4
total_loaves = 0
collored_eggs = 0

while budget > 0:
    total_loaves += 1
    collored_eggs += 3
    budget -= price_per_loaf
    if total_loaves % 3 == 0 and budget >= 0:
        collored_eggs -= total_loaves - 2

if budget <= price_per_loaf:
    budget += price_per_loaf
    total_loaves -= 1
    collored_eggs -= 3


print(f"You made {total_loaves} loaves of Easter bread! Now you have {collored_eggs} eggs and {budget:.2f}BGN left.")

