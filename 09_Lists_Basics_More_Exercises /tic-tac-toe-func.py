def check_winner(board):
    winning_conditions = [
        (board[0][0], board[0][1], board[0][2]),  # First row
        (board[1][0], board[1][1], board[1][2]),  # Second row
        (board[2][0], board[2][1], board[2][2]),  # Third row
        (board[0][0], board[1][0], board[2][0]),  # First column
        (board[0][1], board[1][1], board[2][1]),  # Second column
        (board[0][2], board[1][2], board[2][2]),  # Third column
        (board[0][0], board[1][1], board[2][2]),  # Diagonal left-to-right
        (board[0][2], board[1][1], board[2][0]),  # Diagonal right-to-left
    ]

    for condition in winning_conditions:
        if all(cell == condition[0] for cell in condition):
            if condition[0] == '1':
                return 'First player won'
            elif condition[0] == '2':
                return 'Second player won'
            else:
                return 'Draw!'  # not end of game

    # still no winner found, check for draw
    for row in board:
        if ' ' in row:
            return 'Draw!'  # GAme is not over yet

    # All cells are filled, it's a draw
    return 'Draw!'


board = []
for _ in range(3):
    row = input().split()
    board.append(row)

result = check_winner(board)
print(result)
