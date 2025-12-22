"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xs = 0  # counter for Xs on board
    Os = 0  # counter for Os on board
    for row in board:
        for element in row:
            if element == "X":
                Xs += 1
            elif element == "O":
                Os += 1
    if Xs <= Os:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    modified_board = copy.deepcopy(board)
    possible_moves = actions(modified_board)
    if action not in possible_moves:
        raise ValueError
    else:
        current_player = player(board)
        i = action[0]
        j = action[1]
        modified_board[i][j] = current_player
    return modified_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for j in range(3):
        test_set = []
        for i in range(3):
            test_set.append(board[j][i])
        if test_set == ["X", "X", "X"]:
            return X
        if test_set == ["O", "O", "O"]:
            return O
    for j in range(3):
        test_set = []
        for i in range(3):
            test_set.append(board[i][j])
        if test_set == ["X", "X", "X"]:
            return X
        if test_set == ["O", "O", "O"]:
            return O
    test_set = [board[0][0], board[1][1], board[2][2]]
    if test_set == ["X", "X", "X"]:
        return X
    if test_set == ["O", "O", "O"]:
        return O

    test_set = [board[0][2], board[1][1], board[2][0]]
    if test_set == ["X", "X", "X"]:
        return X
    if test_set == ["O", "O", "O"]:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == "X" or winner(board) == "O":
        return True
    else:
        if actions(board) == set():
            return True
        else:
            return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    possible_moves = list(actions(board))
    best_score_max = -math.inf
    best_score_min = math.inf
    best_move = None
    for move in possible_moves:
        new_board = copy.deepcopy(board)
        new_board = result(new_board, move)
        while terminal(new_board) is False:
            new_board = result(new_board, minimax(new_board))
        score = utility(new_board)
        if player(board) == "X":
            if score > best_score_max:
                best_score_max = score
                best_move = move
        else:
            if score < best_score_min:
                best_score_min = score
                best_move = move
    return best_move