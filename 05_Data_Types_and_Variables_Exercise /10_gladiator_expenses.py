# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield breaks, his armor also needs to be repaired.
# You will receive the price of each item in his equipment.
# Calculate his expenses for the year for renewing his equipment.
# The input will consist of 5 lines:
#     • On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
#     • On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000].
#     • On the third line, you will receive the sword price - a floating-point number in the range [0, 1000].
#     • On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000].
#     • On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000].

lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expenses = 0
shield_breaks = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        total_expenses += helmet_price
    if fight % 3 == 0:
        total_expenses += sword_price
    if fight % 2 == 0 and fight % 3 == 0:
        total_expenses += shield_price
        shield_breaks += 1
        if shield_breaks % 2 == 0:
            total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
