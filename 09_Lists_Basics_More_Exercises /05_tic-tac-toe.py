# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
#     • 0 - empty space
#     • 1 - first player move
#     • 2 - second player move
# Find out who the winner is. If the first player wins, print "First player won".
# If the second player wins, print "Second player won". Otherwise, print "Draw!".

line1 = [int(char) for char in input().split()]
line2 = [int(char) for char in input().split()]
line3 = [int(char) for char in input().split()]

field = [[char for char in line1], [char for char in line2], [char for char in line3]]

columns = [[field[i][0] for i in range(len(field))], [field[i][1] for i in range(len(field))],
           [field[i][2] for i in range(len(field))]]

diagonals = [[field[i][i] for i in range(len(field))], [field[i][len(field)-i-1] for i in range(len(field))]]

no_winner = True

for i in range(len(field)):
    if field[i].count(2) == 3 or columns[i].count(2) == 3:
        print("Second player won")
        no_winner = False
        break
    elif field[i].count(1) == 3 or columns[i].count(2) == 3:
        print("First player won")
        no_winner = False
        break

for diag in diagonals:
    if diag.count(2) == 3:
        print("Second player won")
        no_winner = False
        break
    elif diag.count(1) == 3:
        print("First player won")
        no_winner = False
        break

if no_winner:
    print("Draw!")
