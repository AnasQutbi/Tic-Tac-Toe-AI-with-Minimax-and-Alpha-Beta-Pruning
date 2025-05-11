import math
import time
from tabulate import tabulate

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        for i in range(3):
            print('|'.join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print('-'*5)

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def is_winner(self, player):
        b = self.board
        win_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        return any(all(b[i] == player for i in combo) for combo in win_combos)

    def is_draw(self):
        return ' ' not in self.board and not self.is_winner('X') and not self.is_winner('O')

    def get_available_moves(self):
        return [i for i, val in enumerate(self.board) if val == ' ']

    def reset(self):
        self.board = [' ' for _ in range(9)]


# Minimax
minimax_node_count = 0
def minimax(board, depth, is_max):
    global minimax_node_count
    minimax_node_count += 1

    if board.is_winner('O'):
        return 1
    if board.is_winner('X'):
        return -1
    if board.is_draw():
        return 0

    if is_max:
        best = -math.inf
        for move in board.get_available_moves():
            board.make_move(move, 'O')
            score = minimax(board, depth + 1, False)
            board.board[move] = ' '
            best = max(best, score)
        return best
    else:
        best = math.inf
        for move in board.get_available_moves():
            board.make_move(move, 'X')
            score = minimax(board, depth + 1, True)
            board.board[move] = ' '
            best = min(best, score)
        return best

def get_best_move_minimax(board):
    best_score = -math.inf
    best_move = None
    for move in board.get_available_moves():
        board.make_move(move, 'O')
        score = minimax(board, 0, False)
        board.board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


# Alpha-Beta
alphabeta_node_count = 0
def minimax_ab(board, depth, alpha, beta, is_max):
    global alphabeta_node_count
    alphabeta_node_count += 1

    if board.is_winner('O'):
        return 1
    if board.is_winner('X'):
        return -1
    if board.is_draw():
        return 0

    if is_max:
        value = -math.inf
        for move in board.get_available_moves():
            board.make_move(move, 'O')
            score = minimax_ab(board, depth + 1, alpha, beta, False)
            board.board[move] = ' '
            value = max(value, score)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = math.inf
        for move in board.get_available_moves():
            board.make_move(move, 'X')
            score = minimax_ab(board, depth + 1, alpha, beta, True)
            board.board[move] = ' '
            value = min(value, score)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

def get_best_move_ab(board):
    best_score = -math.inf
    best_move = None
    for move in board.get_available_moves():
        board.make_move(move, 'O')
        score = minimax_ab(board, 0, -math.inf, math.inf, False)
        board.board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


# Performance Comparison
def compare_algorithms():
    global minimax_node_count, alphabeta_node_count

    # Minimax
    board1 = TicTacToe()
    minimax_node_count = 0
    start = time.time()
    get_best_move_minimax(board1)
    end = time.time()
    minimax_time = end - start

    # Alpha-Beta
    board2 = TicTacToe()
    alphabeta_node_count = 0
    start = time.time()
    get_best_move_ab(board2)
    end = time.time()
    alphabeta_time = end - start

    # Results Table
    table = [
        ["Minimax", f"{minimax_time:.6f}", minimax_node_count, "Baseline"],
        ["Alpha-Beta", f"{alphabeta_time:.6f}", alphabeta_node_count,
         f"{minimax_node_count / alphabeta_node_count:.2f}x fewer nodes"]
    ]

    print("\n--- Performance Comparison ---")
    print(tabulate(table, headers=["Algorithm", "Time (s)", "Nodes Explored", "Efficiency"]))


# Game loop
def play_game():
    use_alpha_beta = input("Do you want to use Alpha-Beta Pruning? (y/n): ").strip().lower() == 'y'

    game = TicTacToe()
    print("\nStarting Tic-Tac-Toe Game (You = X, AI = O)")
    while not game.is_winner('X') and not game.is_winner('O') and not game.is_draw():
        game.print_board()
        try:
            move = int(input("Your move (0-8): "))
        except ValueError:
            print("Invalid input!")
            continue

        if move not in game.get_available_moves():
            print("Invalid move. Try again.")
            continue

        game.make_move(move, 'X')
        if game.is_winner('X') or game.is_draw():
            break

        if use_alpha_beta:
            ai_move = get_best_move_ab(game)
        else:
            ai_move = get_best_move_minimax(game)

        game.make_move(ai_move, 'O')
        print(f"AI plays at {ai_move}")

    game.print_board()
    if game.is_winner('X'):
        print("You win!")
    elif game.is_winner('O'):
        print("AI wins!")
    else:
        print("It's a draw!")

    compare_algorithms()


if __name__ == "__main__":
    play_game()