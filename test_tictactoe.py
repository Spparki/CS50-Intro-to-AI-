import pytest
import tictactoe as TT


@pytest.fixture
def board_creator():
    board1 = [[None, None, None],
              [None, None, None],
              [None, None, None]]
    board2 = [["X", None, None],
              [None, None, None],
              [None, "O", None]]
    board3 = [["X", None, None],
              [None, "X", None],
              [None, "O", None]]
    board4 = [["X", None, None],
              [None, "X", None],
              ["O", "O", "X"]]
    board5 = [["X", None, None],
              ["X", "X", None],
              ["O", "O", "O"]]
    board6 = [["X", "X", "O"],
              ["O", "X", "X"],
              ["X", "O", "O"]]
    return board1, board2, board3, board4, board5, board6


def test_player(board_creator):
    answer = []
    for i in range(3):
        answer.append(TT.player(board_creator[i]))
    assert answer == ["X", "X", "O"]


def test_actions(board_creator):
    answer = []
    for i in range(3):
        answer.append(TT.actions(board_creator[i]))
    assert answer == [ 
        set({(0,0),(0,1),(0,2),
            (1,0),(1,1),(1,2),
            (2,0),(2,1),(2,2)}),
        set({(0,1),(0,2),
            (1,0),(1,1),(1,2),
            (2,0),(2,2)}),
        set({(0,1),(0,2),
            (1,0),(1,2),
            (2,0),(2,2)})
    ]


@pytest.fixture
def move_creator():
    move1 = (1,0)
    move2 = (0,1)
    move3 = (2,2)
    move4 = (2,1)
    return move1, move2, move3, move4


def test_result(board_creator, move_creator):
    answer = []
    for i in range(3):
        answer.append(TT.result(board_creator[i], move_creator[i]))
    assert answer == [[[None, None, None],
                       ["X", None, None],
                       [None, None, None]],
                      [["X", "X", None],
                       [None, None, None],
                       [None, "O", None]],
                      [["X", None, None],
                       [None, "X", None],
                       [None, "O", "O"]]]


def test_result_error(board_creator, move_creator):
    with pytest.raises(ValueError):
        TT.result(board_creator[2], move_creator[3])


def test_winner(board_creator):
    answer = []
    for board in board_creator:
        answer.append(TT.winner(board))
    assert answer == [None, None, None, "X", "O", None]


def test_terminal(board_creator):
    answer = []
    for board in board_creator:
        answer.append(TT.terminal(board))
    assert answer == [False, False, False, True, True, True]


def test_utility(board_creator):
    answer = []
    boards = board_creator[3:6]
    for board in boards:
        answer.append(TT.utility(board))
    assert answer == [1, -1, 0]
