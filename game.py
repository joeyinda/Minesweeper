import random

# Function to create the Minesweeper board
def create_board(rows, cols, mines):
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    mine_positions = random.sample(range(rows * cols), mines)

    for position in mine_positions:
        row = position // cols
        col = position % cols
        board[row][col] = '*'

        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0) or not (0 <= row + i < rows) or not (0 <= col + j < cols):
                    continue
                if board[row + i][col + j] != '*':
                    board[row + i][col + j] += 1

    return board

# Function to print the Minesweeper board
def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))

# Function to reveal a cell
def reveal_cell(board, revealed, row, col):
    rows = len(board)
    cols = len(board[0])

    if not (0 <= row < rows) or not (0 <= col < cols) or revealed[row][col]:
        return

    revealed[row][col] = True

    if board[row][col] == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                reveal_cell(board, revealed, row + i, col + j)

# Function to play the Minesweeper game
def play_game():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    mines = int(input("Enter the number of mines: "))

    board = create_board(rows, cols, mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]

    while True:
        print_board(revealed)
        row = int(input("Enter the row (0-{}): ".format(rows - 1)))
        col = int(input("Enter the column (0-{}): ".format(cols - 1)))

        if board[row][col] == '*':
            print("Game over! You hit a mine.")
            revealed[row][col] = True
            break
        else:
            reveal_cell(board, revealed, row, col)

        if all(all(revealed_cell or board_cell == '*' for revealed_cell, board_cell in zip(revealed_row, board_row))
               for revealed_row, board_row in zip(revealed, board)):
            print("Congratulations! You win.")
            break

# Start the game
play_game()
