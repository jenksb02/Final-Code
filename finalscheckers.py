class CheckersGame:
    def __init__(self):
        self.board = [
            ['.' for _ in range(8)] for _ in range(8)
        ]
        self.setup_board()
        self.current_player = 'W'
        self.opponent = 'B' 

    def setup_board(self):
        for row in range(3):
            for col in range((row + 1) % 2, 8, 2):
                self.board[row][col] = 'W'

        for row in range(5, 8):
            for col in range(row % 2, 8, 2):
                self.board[row][col] = 'B'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def get_legal_moves(self):
        legal_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece == self.current_player:
                    if self.current_player == 'W':
                        if row > 0 and col > 0:
                            if self.board[row - 1][col - 1] == '.':
                                legal_moves.append((row, col, row - 1, col - 1))
                        if row > 0 and col < 7:
                            if self.board[row - 1][col + 1] == '.':
                                legal_moves.append((row, col, row - 1, col + 1))
                    else: 
                        if row < 7 and col > 0:
                            if self.board[row + 1][col - 1] == '.':
                                legal_moves.append((row, col, row + 1, col - 1))
                        if row < 7 and col < 7:
                            if self.board[row + 1][col + 1] == '.':
                                legal_moves.append((row, col, row + 1, col + 1))
        return legal_moves

    def make_move(self, move):
        start_row, start_col, end_row, end_col = move
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = '.'

    def undo_move(self, move):
        start_row, start_col, end_row, end_col = move
        self.board[start_row][start_col] = self.board[end_row][end_col]
        self.board[end_row][end_col] = '.'

    def evaluate_board(self):
        score = 0
        opponent_moves = self.get_legal_moves_for_opponent()
        if len(opponent_moves) == 0:
            score += 10  
        for move in self.get_legal_moves():
            if abs(move[0] - move[2]) > 1:  
                score += 5  
            if self.is_safe_move(move): 
                score += 3  
        return score

    def get_legal_moves_for_opponent(self):
        legal_moves = []
        opponent = 'W' if self.current_player == 'B' else 'B'
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece == opponent:
                    if opponent == 'W':
                        if row < 7 and col > 0:
                            if self.board[row + 1][col - 1] == '.':
                                legal_moves.append((row, col, row + 1, col - 1))
                        if row < 7 and col < 7:
                            if self.board[row + 1][col + 1] == '.':
                                legal_moves.append((row, col, row + 1, col + 1))
                    else:  
                        if row > 0 and col > 0:
                            if self.board[row - 1][col - 1] == '.':
                                legal_moves.append((row, col, row - 1, col - 1))
                        if row > 0 and col < 7:
                            if self.board[row - 1][col + 1] == '.':
                                legal_moves.append((row, col, row - 1, col + 1))
        return legal_moves

    def is_safe_move(self, move):
        _, _, end_row, end_col = move
        if end_row == 0 or end_row == 7 or end_col == 0 or end_col == 7:
            return True  
        return False

    def minimax(self, depth, alpha, beta, maximizing_player):
        pass

    def get_best_move(self, depth):
        pass


game = CheckersGame()
game.print_board()
evaluation_result = game.evaluate_board()
print("Evaluation result:", evaluation_result)
