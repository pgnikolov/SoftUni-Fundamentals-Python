# Two teams, named "A" and "B" have 11 players each.
# The players on each team are numbered from 1 to 11.
# Any player may be sent off the field by being given a red card. If one of the teams has less than 7 players remaining,
# the referee stops the game immediately, and the team with less than 7 players loses.
# The card is a string with the team's letter ("A" or "B") followed by a single dash and the player's number.
# the card "B-7" means player #7 from team B received a card.
# You will be given a sequence of cards (could be empty), separated by a single space. You should print the count of
# remaining players on each team at the end of the game :"Team A - {players_count};Team B - {players_count}".
# If the referee terminated the game, print an additional line: "Game was terminated".

# A = list(range(1, 12))
# B = list(range(1, 12))
#
# sequence_cards = input()
# list_cards = sequence_cards.split(" ")
# not_terminated = True
#
# teamA = ['A-' + str(char) for char in A]
# teamB = ['B-' + str(char) for char in B]
#
# for i in range(len(list_cards)):
#     if list_cards[i] in teamA:
#         teamA.remove(list_cards[i])
#     elif list_cards[i] in teamB:
#         teamB.remove(list_cards[i])
#     if len(teamA) < 7 or len(teamB) < 7:
#         not_terminated = False
#
# if not not_terminated:
#     print(f"Team A - {len(teamA)}; Team B - {len(teamB)}")
#     print("Game was terminated")
# else:
#     print(f"Team A - {len(teamA)}; Team B - {len(teamB)}")

string_of_cards = input().split()
a_cards = []
b_cards = []

for card in string_of_cards:
    if "A-" in card:
        a_cards.append(card)
    elif "B-" in card:
        b_cards.append(card)

redcards_a = len(set(a_cards))
redcards_b = len(set(b_cards))
if redcards_a > 5:
    red_a = 5
if redcards_b > 5:
    red_b = 5
print(f'Team A - {11 - redcards_a}; Team B - {11 - redcards_b}')
if redcards_a == 5 or redcards_b == 5:
    print('Game was terminated')
    