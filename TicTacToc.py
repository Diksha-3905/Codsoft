import math

class TicTacToe:
    def __init__(self, size=3, win_condition=3):
        self.size = size
        self.win_condition = win_condition
        self.board = [' ' for _ in range(size * size)]
    
    def print_board(self):
        for row in [self.board[i*self.size:(i+1)*self.size] for i in range(self.size)]:
            print('| ' + ' | '.join(row) + ' |')
    
    def check_win(self, player):
        # Check rows
        for row in range(self.size):
            if all([self.board[row * self.size + i] == player for i in range(self.win_condition)]):
                return True
        # Check columns
        for col in range(self.size):
            if all([self.board[col + self.size * i] == player for i in range(self.win_condition)]):
                return True
        # Check diagonals
        if all([self.board[i * (self.size + 1)] == player for i in range(self.win_condition)]):
            return True
        if all([self.board[(i + 1) * (self.size - 1)] == player for i in range(self.win_condition)]):
            return True
        return False

    def check_full(self):
        return ' ' not in self.board

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def undo_move(self, position):
        self.board[position] = ' '

    def get_valid_moves(self):
        return [i for i in range(self.size * self.size) if self.board[i] == ' ']

    def get_board_copy(self):
        return self.board.copy()

    def minimax(self, is_maximizing, alpha, beta):
        if self.check_win('X'):
            return -1
        elif self.check_win('O'):
            return 1
        elif self.check_full():
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for move in self.get_valid_moves():
                self.make_move(move, 'O')
                eval = self.minimax(False, alpha, beta)
                self.undo_move(move)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in self.get_valid_moves():
                self.make_move(move, 'X')
                eval = self.minimax(True, alpha, beta)
                self.undo_move(move)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def find_best_move(self):
        best_move = None
        best_value = -math.inf
        for move in self.get_valid_moves():
            self.make_move(move, 'O')
            move_value = self.minimax(False, -math.inf, math.inf)
            self.undo_move(move)
            if move_value > best_value:
                best_value = move_value
                best_move = move
        return best_move

def play_game(size=3, win_condition=3):
    game = TicTacToe(size, win_condition)
    print("Welcome to Tic-Tac-Toe!")
    game.print_board()
    
    while True:
        # Human move
        move = int(input(f"Enter your move (0-{size*size - 1}): "))
        if not game.make_move(move, 'X'):
            print("Invalid move! Try again.")
            continue

        game.print_board()

        if game.check_win('X'):
            print("Congratulations! You win!")
            break
        elif game.check_full():
            print("It's a tie!")
            break

        # AI move
        print("AI is making a move...")
        ai_move = game.find_best_move()
        game.make_move(ai_move, 'O')

        game.print_board()

        if game.check_win('O'):
            print("AI wins! Better luck next time.")
            break
        elif game.check_full():
            print("It's a tie!")
            break

# Start the game
play_game(size=3, win_condition=3)
