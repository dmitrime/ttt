# -*- coding: utf-8 -*-
import copy
import random
from players import UserPlayer, AIPlayer

class State:
    '''
    Holds the state of the game.
    '''
    def __init__(self):
        self.board = self._empty_board()

    def _rows(self, b):
        return [b[:3], b[3:6], b[6:]]

    def _cols(self, b):
        '''
        Returns the columns of the board.
        '''
        return [[b[i], b[i+3], b[i+6]] for i in range(3)]

    def _diag(self, b):
        '''
        Returns the diagonals of the board.
        '''
        return [[b[0], b[4], b[8]], [b[2], b[4], b[6]]]

    def _empty_board(self):
        return [None]*9

    def isBoardFull(self):
        return all(self.board)

    def isWinning(self, player):
        '''
        Checks if "player" has won.
        '''
        win = [player]*3
        pos = self._rows(self.board) + \
              self._cols(self.board) + \
              self._diag(self.board)
        return any([win == x for x in pos])

    def show(self):
        for i in range(len(self.board)):
            if i % 3 == 0:
                print
            print '{} '.format(self.board[i] if self.board[i] else i+1),
        print '\n'

    def canPut(self, i):
        return self.board[i] is None

    def put(self, xo, i):
        if not self.canPut(i):
            raise ValueError("Choose an empty square!")
        self.board[i] = xo

    def unput(self, i):
        self.board[i] = None

    def copy(self):
        return copy.deepcopy(self)


class Game:
    def __init__(self):
        self.xo = ['X', 'O']
        self.s = State()

    def assignXO(self):
        p = random.randint(0, 1)
        return self.xo[p], self.xo[1-p]

    def first(self):
        return self.xo[0]

    def isGameOver(self):
        return self.s.isBoardFull() or \
            self.s.isWinning(self.xo[0]) or \
            self.s.isWinning(self.xo[1])

    def play(self):
        print 'New game'
        p1, p2 = self.assignXO()
        usr = UserPlayer(p1, p2)
        ai = AIPlayer(p2, p1)

        if usr.xo == self.first():
            print 'User starts the game with \'{}\''.format(self.first())
            self.s.show()
            usr.makeMove(self.s)
        else:
            print 'AI starts the game with \'{}\''.format(self.first())

        while not self.isGameOver():
            ai.makeMove(self.s)
            if self.isGameOver():
                break
            usr.makeMove(self.s)

        if self.s.isWinning(usr.xo):
            print 'You\'ve won, impressive!'
        elif self.s.isWinning(ai.xo):
            print 'You lose, sorry...'
        else:
            print 'It\'s a draw.'


if __name__ == '__main__':
    Game().play()
