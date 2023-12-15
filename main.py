"""
This is a Tic-Tac-Toe game implemented in Python. It consists of a Tictactoe class, a Player class,
and an AI class. The Tictactoe class represents the game board and contains methods for making moves,
checking for a winner, and determining if the game has ended. The Player class represents a human player and
allows them to make moves by selecting a number corresponding to a position on the board. The AI class represents
an unbeatable AI player that uses the minimax algorithm to determine the best move to make.

you can change the conditions of the game at the end of the file (line 158:).
"""
import math
from time import sleep

# stores the corresponding coordinates to the numbers
num_to_coordinate = {1: (0, 0),
                     2: (0, 1),
                     3: (0, 2),
                     4: (1, 0),
                     5: (1, 1),
                     6: (1, 2),
                     7: (2, 0),
                     8: (2, 1),
                     9: (2, 2)}


class Tictactoe:
    def __init__(self):
        # Initializes the game board and sets the turn to 'X'.
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.turn = 'X'

    def runner(self, X_player, O_player):
        # Runs the game loop until there is a winner or the game ends.
        # It alternates between the X player and the O player to make moves.
        while not self.end():
            sleep(0.66)
            print(f"\n{self.turn}'s turn ")
            if self.turn == 'X':
                X_player.get_move()
                self.turn = 'O'
            elif self.turn == 'O':
                O_player.get_move()
                self.turn = 'X'

    def print(self):
        # Prints the current state of the game board.
        for i in self.board:
            for j in i:
                print(j, end=' ')
            print()

    def make_move(self, place, shape):
        # Makes a move on the game board by updating the specified position with the given shape ('X' or 'O').
        self.board[place[0]][place[1]] = shape

    def undo_move(self, num):
        # Undoes a move by updating the specified position with the original number.
        co = num_to_coordinate[num]
        self.board[co[0]][co[1]] = num

    def available_moves(self):
        # Returns a list of available moves on the game board.
        moves = []
        for i in self.board:
            for j in i:
                if j in range(10):
                    moves.append(j)
        return moves

    def winner(self):
        # Checks for a winner by checking all possible winning combinations on the game board.
        for i in range(3):
            if self.board[i] == ['X', 'X', 'X']:
                return "X"
            if self.board[i] == ["O", "O", "O"]:
                return "O"
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        return None

    def empty(self):
        # Counts the number of empty positions on the game board.
        count = 0
        for i in [j for i in self.board for j in i]:
            if str(i) not in 'XO':
                count += 1
        return count

    def end(self):
        # Checks if the game has ended by checking for a winner or no available moves.
        return self.winner() or not self.available_moves()


class Player:
    def __init__(self, game, shape):
        # Initializes the player with the specified game instance and shape ('X' or 'O').
        self.game = game
        self.shape = shape

    def make_move(self, num, shape):
        # Makes a move on the game board by converting the number to coordinates and calling the make_move() function
        # in the game(Tic-Tac-Toe class).
        self.game.make_move(num_to_coordinate[num], shape)

    def get_move(self):
        # Prompts the player to choose a number corresponding to a position on the game board and makes the move
        # if it is valid.
        self.game.print()
        move = int(input('choose a number: '))
        while move not in game.available_moves():
            print('invalid move!')
            move = int(input('choose a number: '))
        self.make_move(move, self.shape)


class AI(Player):
    # The AI class is a subclass of the Player class
    def get_move(self):
        # Overrides the get_move method of the Player class to make an unbeatable move using the minimax algorithm.
        self.game.print()
        if len(self.game.available_moves()) == 9:
            move = 2
        else:
            move = self.minimax(self.shape)['position']

        self.make_move(move, self.shape)

    def minimax(self, shape):
        """
        Implements the minimax algorithm to determine the best move for the AI player. It recursively simulates
        the game after making each possible move and assigns a score to each move based on the outcome of the game.
        The AI player chooses the move with the best score for the specific shape.
        """

        # determine if the current player is the max player or otherwise
        max_player = True if shape == 'X' else False
        other_player = 'O' if max_player else 'X'

        # check base case to see if there is a winner
        if self.game.winner():
            return {'position': None,
                    'score': 1 * (self.game.empty() + 1) if self.game.winner() == 'X' else -1 * (self.game.empty() + 1)}

        elif not self.game.empty():
            return {'position': None, 'score': 0}

        # creating a base score to compare with action scores
        if max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for move in self.game.available_moves():
            # 1 : make a move
            self.make_move(move, shape)

            # 2 : recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(other_player)

            # 3 : undo the move
            self.game.undo_move(move)
            sim_score['position'] = move

            # 4 : update the dictionaries if necessary
            if max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best


if __name__ == "__main__":
    """
    The main part of the code creates an instance of the Tictactoe class, initializes a human player ('X') and
    an AI player ('O'), and runs the game loop using the runner method. After the game ends, it prints the final state
    of the game board and the result of the game (winner or draw).
    """
    game = Tictactoe()
    X = Player(game, "X")
    O = AI(game, "O")

    game.runner(X, O)
    print()
    game.print()
    print()
    if game.winner():
        print(f'{game.winner()} has won!')
    else:
        print("It's a draw!")
        
