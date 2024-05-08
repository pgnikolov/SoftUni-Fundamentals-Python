# string with even integers, separated by a "@" - this is our neighborhood.
# series of Jump commands will follow until you receive "Love!"
# Every house in the neighborhood needs a certain number of hearts delivered
# Cupid starts at the position of the first house (index 0) and must jump by a given length.
# The jump commands will be in this format: "Jump {length}".
# the needed hearts for the visited house are decreased by 2
# • If the needed hearts for a certain house become equal to 0,
#   print on the console "Place {house_index} has Valentine's Day."
# • If Cupid jumps to a house where the needed hearts are already 0,
# print on the console "Place {house_index} already had Valentine's Day."
# • Keep in mind that Cupid can have a larger jump length than the size of the neighborhood,
# and if he does jump outside of it, he should start from the first house again (index 0).
# In the end, print Cupid's last position and whether his mission was successful or not:
#     • "Cupid's last position was {last_position_index}."
#     • If each house has had Valentine's Day, print:
#         ◦ "Mission was successful."
#     • If not, print the count of all houses that didn't celebrate Valentine's Day:
#         ◦ "Cupid has failed {houseCount} places."

neighborhood_list = [int(number) for number in input().split("@")]
cupid_position = 0

while True:
    system_input = input().split()
    command = system_input[0]
    if command == "Love!":
        neighborhood_list = [house for house in neighborhood_list if house > 0]
        print(f"Cupid's last position was {cupid_position}.")
        if len(neighborhood_list) == 0:
            print("Mission was successful.")
        else:
            print(f"Cupid has failed {len(neighborhood_list)} places.")
        break

    jump_length = int(system_input[1])
    cupid_position += jump_length
    if cupid_position >= len(neighborhood_list):
        cupid_position = 0

    if neighborhood_list[cupid_position] == 0:
        print(f"Place {cupid_position} already had Valentine's day.")
    else:
        neighborhood_list[cupid_position] -= 2
        if neighborhood_list[cupid_position] == 0:
            print(f"Place {cupid_position} has Valentine's day.")