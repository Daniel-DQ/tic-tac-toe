"""
Tic Tac Toe Player
TODO
when the recursive function calls itself and changes a variable like board ..
apparently it changes that variable all across the call stack , well that's a FUCKING BUG , good luck with that
"""

import math
import random

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

    make it so that if the board is full it's the X's turn DONE.
    """
    if board == initial_state():
        return X

    li = [j for i in board for j in i]

    """
    if li.count("X") < li.count("O"):
        return X
    """
    if li.count("O") < li.count("X"):
        # if the board is full returns X
        if None not in li:
            return X
        return O

    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(len(board)) for j in range(len(board)) if board[i][j] is None}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    temp = board.copy()
    temp[action[0]][action[1]] = player(board)
    return temp


def winner(board):
    """
    Returns the winner of the game, if there is one.
    TODO : seems fine
    check this function .. it's not working properly .. maybe in some edge cases
    """
    for shape in ["X", "O"]:
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == shape:
                return shape
            if board[i][0] == board[i][1] == board[i][2] == shape:
                return shape
        if board[0][0] == board[1][1] == board[2][2] == shape or board[0][2] == board[1][1] == board[2][0] == shape:
            return shape

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for shape in ["X", "O"]:
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == shape:
                return True
            if board[i][0] == board[i][1] == board[i][2] == shape:
                return True
        if board[0][0] == board[1][1] == board[2][2] == shape or board[0][2] == board[1][1] == board[2][0] == shape:
            return True

    if None not in [j for i in board for j in i]:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    check the winner too . DONE
    """
    if terminal(board) and winner(board):
        if winner(board) == X:
            return 1 * (num_empty(board)+1)
        elif winner(board) == O:
            return -1 * (num_empty(board)+1)
    return 0

    # return utility(result(board, minimax(board)))


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    """
    utis = []
    acts = []

    for action in actions(board):
        uti = utility(result(board, action))
        utis.append(uti)
        acts.append(action)
        board[action[0]][action[1]] = None

    return acts[utis.index(max(utis))] if player(board) == X else acts[utis.index(min(utis))]
    """
    if len(actions(board)) == 9:
        square = (1, 1)
    else:
        square = minimax2(board, player(board))['position']
    return square


def minimax2(board, c_player):
    max_player = True if c_player == X else False
    other_player = O if max_player else X

    # check base case to see if there is a winner
    if winner(board):
        return {'position': None,
                'score': 1 * (num_empty(board) + 1) if winner(board) == X else -1 * (num_empty(board) + 1)}

    elif not num_empty(board):
        return {'position': None, 'score': 0}

    if max_player:
        best = {'position': None, 'score': -math.inf}
    else:
        best = {'position': None, 'score': math.inf}

    for action in actions(board):
        # step 1 : make a move, try that spot
        board = result(board, action)

        # step 2: recurse using minimax to simulate a game after making that move
        sim_score = minimax2(board, other_player)

        # step 3: undo the move
        board[action[0]][action[1]] = None
        sim_score['position'] = action

        # step 4 : update the dictionaries if necessary
        if max_player:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score
    return best


def num_empty(board):
    return [j for i in board for j in i].count(None)
