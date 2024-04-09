# Two teams, named "A" and "B" have 11 players each.
# The players on each team are numbered from 1 to 11.
# Any player may be sent off the field by being given a red card. If one of the teams has less than 7 players remaining,
# the referee stops the game immediately, and the team with less than 7 players loses.
# The card is a string with the team's letter ("A" or "B") followed by a single dash and the player's number.
# the card "B-7" means player #7 from team B received a card.
# You will be given a sequence of cards (could be empty), separated by a single space. You should print the count of
# remaining players on each team at the end of the game :"Team A - {players_count};Team B - {players_count}".
# If the referee terminated the game, print an additional line: "Game was terminated".

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
