# Tic-Tac-Toe

# Function to print the game board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over:
        # Get the current player's move
        print("Player", current_player)
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))

        # Update the board
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move! Try again.")
            continue

        # Print the updated board
        print_board(board)

        # Check if the current player has won
        if check_win(board, current_player):
            print("Player", current_player, "wins!")
            game_over = True
        elif all(board[i][j] != " " for i in range(3) for j in range(3)):
            # Check if it's a draw
            print("It's a draw!")
            game_over = True

        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
