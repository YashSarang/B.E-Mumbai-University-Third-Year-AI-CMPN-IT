import random
import numpy as np

N_QUEEN = 4

def in_conflict(column, row, other_column, other_row):
   
    if column == other_column:
        return True  # Same column
    if row == other_row:
        return True  # Same row
    if abs(column - other_column) == abs(row - other_row):
        return True  # Diagonal

    return False


def in_conflict_with_another_queen(row, column, board):
   
    for other_column, other_row in enumerate(board):
        if in_conflict(column, row, other_column, other_row):
            if row != other_row or column != other_column:
                return True
    return False


def count_conflicts(board):
  
    cnt = 0

    for queen in range(0, len(board)):
        for other_queen in range(queen + 1, len(board)):
            if in_conflict(queen, board[queen], other_queen, board[other_queen]):
                cnt += 1

    return cnt


def evaluate_state(board):
   
    return (len(board) - 1) * len(board) / 2 - count_conflicts(board)


def print_board(board):
   
    for row in range(len(board)):
        line = ''
        for column in range(len(board)):
            if board[column] == row:
                line += 'Q' if in_conflict_with_another_queen(row, column, board) else 'q'
            else:
                line += '_'
        print(line)
    print("")


def init_board(nqueens):
  
    board = []

    for column in range(nqueens):
        board.append(random.randint(0, nqueens - 1))
    print('Initial State:')
    print_board(board)
    return board


def Hill_Climbing(board):
  
    i = 0
    optimum = (len(board) - 1) * len(board) / 2
    evaluation = [evaluate_state(board)]

    while evaluate_state(board) != optimum:
        i += 1
       
        max_score_of_each_column = []
        row_resulting_in_max_score = []

        for col in range(len(board)):
            col_scores = []

            for row in range(len(board)):
                new_board = board.copy()
                new_board[col] = row
                col_scores.append(evaluate_state(new_board))

            if max(col_scores) > evaluate_state(board):
                max_score_of_each_column.append(max(col_scores))
                row_resulting_in_max_score.append(np.argmax(col_scores))
            else:
                max_score_of_each_column.append(False)
                row_resulting_in_max_score.append(False)

        if max(max_score_of_each_column):
            maximizing_col = np.argmax(max_score_of_each_column)
            maximizing_row = row_resulting_in_max_score[maximizing_col]
            board[maximizing_col] = maximizing_row

        evaluation.append(evaluate_state(board))

    if evaluate_state(board) == optimum:
        print('\nSolved Puzzle!')

    print('\nFinal State:')
    print_board(board)
   
if __name__ == "__main__":
    Hill_Climbing(init_board(N_QUEEN))

