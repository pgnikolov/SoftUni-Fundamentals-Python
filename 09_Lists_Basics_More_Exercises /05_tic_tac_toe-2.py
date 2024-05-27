row_1 = input().split()
row_2 = input().split()
row_3 = input().split()
game_field = row_1, row_2, row_3

if game_field[0][0] == game_field[0][1] == game_field[0][2] == "1" or \
        game_field[1][0] == game_field[1][1] == game_field[1][2] == "1" or \
        game_field[2][0] == game_field[2][1] == game_field[2][2] == "1" or \
        game_field[0][0] == game_field[1][0] == game_field[2][0] == "1" or \
        game_field[0][1] == game_field[1][1] == game_field[2][1] == "1" or \
        game_field[0][2] == game_field[1][2] == game_field[2][2] == "1" or \
        game_field[0][0] == game_field[1][1] == game_field[2][2] == "1" or \
        game_field[0][2] == game_field[1][1] == game_field[2][0]:
    print("First player won")

elif game_field[0][0] == game_field[0][1] == game_field[0][2] == "2" or \
        game_field[1][0] == game_field[1][1] == game_field[1][2] == "2" or \
        game_field[2][0] == game_field[2][1] == game_field[2][2] == "2" or \
        game_field[0][0] == game_field[1][0] == game_field[2][0] == "2" or \
        game_field[0][1] == game_field[1][1] == game_field[2][1] == "2" or \
        game_field[0][2] == game_field[1][2] == game_field[2][2] == "2" or \
        game_field[0][0] == game_field[1][1] == game_field[2][2] == "2" or \
        game_field[0][2] == game_field[1][1] == game_field[2][0]:
    print("Second player won")
else:
    print("Draw!")
    