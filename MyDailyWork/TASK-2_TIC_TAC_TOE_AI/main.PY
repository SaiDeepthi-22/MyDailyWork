import math

# ----------------------------
# Tic Tac Toe AI (Minimax)
# Human = X
# AI    = O
# ----------------------------

board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for row in range(3):
        print("| " + " | ".join(board[row*3:(row+1)*3]) + " |")
    print()

def print_positions():
    print("\nPositions reference:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |\n")

def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],      # rows
        [0,3,6],[1,4,7],[2,5,8],      # cols
        [0,4,8],[2,4,6]               # diagonals
    ]
    for cond in win_conditions:
        if all(board[i] == player for i in cond):
            return True
    return False

def is_draw():
    return " " not in board

def available_moves():
    return [i for i in range(9) if board[i] == " "]

# ----------------------------
# Minimax Algorithm
# ----------------------------
def minimax(is_maximizing):
    if check_winner("O"):  # AI wins
        return 1
    if check_winner("X"):  # Human wins
        return -1
    if is_draw():
        return 0

    if is_maximizing:  # AI turn
        best_score = -math.inf
        for move in available_moves():
            board[move] = "O"
            score = minimax(False)
            board[move] = " "
            best_score = max(best_score, score)
        return best_score

    else:  # Human turn
        best_score = math.inf
        for move in available_moves():
            board[move] = "X"
            score = minimax(True)
            board[move] = " "
            best_score = min(best_score, score)
        return best_score

# ----------------------------
# AI Move
# ----------------------------
def ai_move():
    best_score = -math.inf
    best_move = None

    for move in available_moves():
        board[move] = "O"
        score = minimax(False)
        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    board[best_move] = "O"

# ----------------------------
# Human Move
# ----------------------------
def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in available_moves():
                board[move] = "X"
                break
            else:
                print("❌ Invalid move! That spot is taken or not in range.")
        except:
            print("❌ Please enter a valid number from 1 to 9.")

# ----------------------------
# Main Game Loop
# ----------------------------
def play_game():
    print("🎮 Tic-Tac-Toe AI")
    print("Human = X | AI = O")
    print("AI uses Minimax Algorithm (Unbeatable)")
    print_positions()

    print_board()

    while True:
        # Human turn
        human_move()
        print_board()

        if check_winner("X"):
            print("🎉 You win! (This should not happen if AI is perfect 😄)")
            break
        if is_draw():
            print("🤝 It's a draw!")
            break

        # AI turn
        print("🤖 AI is thinking...")
        ai_move()
        print_board()

        if check_winner("O"):
            print("💀 AI wins! Better luck next time.")
            break
        if is_draw():
            print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    play_game()
