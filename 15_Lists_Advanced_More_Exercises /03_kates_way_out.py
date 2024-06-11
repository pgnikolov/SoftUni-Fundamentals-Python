# On the first line, you will be given how many rows there are in the maze. On the following n lines,
# you will be given the maze itself. Here is a legend for the maze:
#     • "#" - means a wall; Kate cannot go through there
#     • " " - means empty space; Kate can go through there
#     • "k" - the initial position of Kate; start looking for a way out from there
#  are two options: Kate either gets out or not:
#     • If Kate can get out, print the following:
# "Kate got out in {number_of_moves} moves".
# Note: If there are two or more ways out, she always chooses the longest one.
#     • Otherwise, print: "Kate cannot get out"


# def find_exit(row, col, moves):
#     if not (0 <= row < len(matrix) and 0 <= col < len(matrix[0])):
#         return moves
#
#     if matrix[row][col] == "#":
#         return 0
#
#     matrix[row][col] = "#"
#
#     exit1 = find_exit(row + 1, col, moves + 1)
#     exit2 = find_exit(row - 1, col, moves + 1)
#     exit3 = find_exit(row, col + 1, moves + 1)
#     exit4 = find_exit(row, col - 1, moves + 1)
#
#     return max(exit1, exit2, exit3, exit4)
#
#
# matrix = []
# cordinates_kate = []
#
# for row in range(int(input())):
#     matrix.append(list(input()))
#
#     if "k" in matrix[row]:
#         cordinates_kate = [row, matrix[row].index("k")]
#
# longest_way = find_exit(cordinates_kate[0], cordinates_kate[1], 0)
#
# if not longest_way:
#     print(f"Kate cannot get out")
# else:
#     print(f"Kate got out in {longest_way} moves")


rows = int(input())

matrix, moves, startrow, startcol = [], [], 0, 0

for row in range(rows):
    matrix.append(list(input()))
    if "k" in matrix[row]:
        startrow, startcol = row, matrix[row].index("k")

cols = len(matrix[0])


def find_exit(row, col, move):
    if not 0 <= row < rows or not 0 <= col < cols or matrix[row][col] in "#*":
        return

    move += 1
    if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
        moves.append(move)

    matrix[row][col] = "*"
    [find_exit(row, col, move) for row, col in
     ((row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col))]
    matrix[row][col] = " "
    move -= 1


find_exit(startrow, startcol, 0)

if moves:
    print(f"Kate got out in {max(moves)} moves")
else:
    print("Kate cannot get out")
