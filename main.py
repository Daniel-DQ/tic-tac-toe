#  this is tic-tac-toe
"""
TODO LIST:
1. create board ... done!
2. create players ... done!
3. Tictactoe class ( rules and logic) ... done!
4. unbeatable AI ... phind can help
"""
import math


class Tictactoe:
    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.turn = 'X'

    def runner(self, X_player, O_player):
        while not self.end():
            print(f"\n{self.turn}'s turn ")
            if self.turn == 'X':
                X_player.get_move()
                self.turn = 'O'
            elif self.turn == 'O':
                O_player.get_move()
                self.turn = 'X'

    def print(self):
        for i in self.board:
            for j in i:
                print(j, end=' ')
            print()

    def make_move(self, place, shape):
        self.board[place[0]][place[1]] = shape

    def available_moves(self):
        moves = []
        for i in self.board:
            for j in i:
                if j in range(10):
                    moves.append(j)
        return moves

    def winner(self):
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

    def end(self):
        return self.winner() or not self.available_moves()


class Player:
    def __init__(self, game, shape):
        self.game = game
        self.shape = shape

    def make_move(self, num):
        num_to_coordinance = {1: (0, 0),
                              2: (0, 1),
                              3: (0, 2),
                              4: (1, 0),
                              5: (1, 1),
                              6: (1, 2),
                              7: (2, 0),
                              8: (2, 1),
                              9: (2, 2)}
        self.game.make_move(num_to_coordinance[num], self.shape)

    def get_move(self):
        game.print()
        move = int(input('choose a number: '))
        while move not in game.available_moves():
            print('invalid move!')
            move = int(input('choose a number: '))
        self.make_move(move)


if __name__ == "__main__":
    game = Tictactoe()
    X = Player(game, "X")
    O = Player(game, "O")

    game.runner(X, O)

    game.print()
    if game.winner():
        print(f'winner is {game.winner()}!')
    else:
        print("It's a draw!")
