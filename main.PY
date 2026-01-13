import math
class TicTacToe:
    def __init__(self):
        self.board=[" " for _ in range(9)]
    def print_board(self):
        print(self.board[0], "|", self.board[1], "|", self.board[2])
        print("--+---+--")
        print(self.board[3], "|", self.board[4], "|", self.board[5])
        print("--+---+--")
        print(self.board[6], "|", self.board[7], "|", self.board[8])
    def check_winner(self,player):
        win_condition=[
            [0,1,2],[3,4,5],[6,7,8], #rows
            [0,3,6],[1,4,7],[2,5,8], #cols
            [0,4,8],[2,4,6]          #diagnol
        ]
        for condition in win_condition:
            if all(self.board[i]== player for i in condition):
                return True
        return False
    def is_draw(self):
        return " " not in self.board
    def available_moves(self):
        moves = []
        for i in range(9):
            if self.board[i] == " ":
               moves.append(i)
        return moves
    def minimax(self,is_maximizing):
        if self.check_winner("O"):
            return 1
        if self.check_winner("X"):
            return -1
        if self.is_draw():
            return 0
        if is_maximizing:
            best_score=-math.inf
            for move in self.available_moves():
              self.board[move]="O"
              score = self.minimax(False)
              self.board[move] = " "
              best_score = max(best_score, score)
            return best_score
        else: 
            best_score = math.inf
            for move in self.available_moves():
              self.board[move] = "X"
              score = self.minimax(True)
              self.board[move] = " "
              best_score = min(best_score, score)
            return best_score
    def ai_move(self):
        best_score=-math.inf
        best_move=None
        for move in self.available_moves():
            self.board[move] = "O"
            score = self.minimax(False)
            self.board[move] = " "
            if score > best_score:
                best_score = score
                best_move = move

        self.board[best_move] = "O"
    def human_move(self):
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move in self.available_moves():
                    self.board[move] = "X"
                    break
                else:
                    print("Invalid move! Try again.")
            except:
                print("Enter only number from 1 to 9.")
    def play(self):
        print(" Tic Tac Toe: Human (X) vs AI (O)")
        self.print_board()
        while True:
            self.human_move()
            self.print_board()
            if self.check_winner("X"):
                print(" You win!")
                break
            if self.is_draw():
                print(" It's a draw!")
                break
            print(" AI is making a move...")
            self.ai_move()
            self.print_board()
            if self.check_winner("O"):
                print(" AI wins!")
                break
            if self.is_draw():
                print(" It's a draw!")
                break
game=TicTacToe()
game.play()