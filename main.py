import random 

# Constants for the game
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'
BOARD_SIZE = 3

# Initialize the board
def initialize_board():
    return [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]

# Print the board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * (BOARD_SIZE * 2 - 1))

# Check if the current player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)):
        return True
    return False

# Check if the board is full
def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Get available moves
def get_available_moves(board):
    return [(row, col) for row in range(BOARD_SIZE) for col in range(BOARD_SIZE) if board[row][col] == EMPTY]

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_O):
        return 10 - depth
    if check_winner(board, PLAYER_X):
        return depth - 10
    if is_full(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for row, col in get_available_moves(board):
            board[row][col] = PLAYER_O
            score = minimax(board, depth + 1, False)
            board[row][col] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row, col in get_available_moves(board):
            board[row][col] = PLAYER_X
            score = minimax(board, depth + 1, True)
            board[row][col] = EMPTY
            best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for row, col in get_available_moves(board):
        board[row][col] = PLAYER_O
        score = minimax(board, 0, False)
        board[row][col] = EMPTY
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move

# Main game loop
def main():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the AI is O.")

    while True:
        # Player's turn
        print_board(board)
        if is_full(board):
            print("It's a tie!")
            break
        
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if (row, col) in get_available_moves(board):
                    board[row][col] = PLAYER_X
                    break
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as integers between 0 and 2.")
        
        if check_winner(board, PLAYER_X):
            print_board(board)
            print("Congratulations! You win!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # AI's turn
        print("AI's turn...")
        row, col = ai_move(board)
        board[row][col] = PLAYER_O
        
        if check_winner(board, PLAYER_O):
            print_board(board)
            print("AI wins! Better luck next time.")
            break

if __name__ == "__main__":
    main()
