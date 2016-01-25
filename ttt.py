# -*- coding: utf-8 -*-
import copy
import random
from player import UserPlayer
from ai import AIPlayer

class State:
    '''
    Holds the state of the game.
    '''
    def __init__(self, size):
        self.n = size
        self.board = self._empty_board()

    def _rows(self, b):
        n = self.n
        return [b[i:i+n] for i in range(0, n*n, n)]

    def _cols(self, b):
        '''
        Returns the columns of the board.
        '''
        n = self.n
        return [[b[i+j] for j in range(0, n*n, n)] for i in range(n)]

    def _diag(self, b):
        '''
        Returns the diagonals of the board.
        '''
        n = self.n
        return [[b[i+i*n] for i in range(n)],
                       [b[n-i-1+i*n] for i in range(n)]]

    def _empty_board(self):
        return [None]*(self.n*self.n)

    def isBoardFull(self):
        return all(self.board)

    def isWinning(self, player):
        '''
        Checks if "player" has won.
        '''
        win = [player]*self.n
        pos = self._rows(self.board) + \
              self._cols(self.board) + \
              self._diag(self.board)
        return any([win == x for x in pos])

    def show(self):
        for i in range(len(self.board)):
            if i % self.n == 0:
                print '\n'
            print '{}\t'.format(self.board[i] if self.board[i] else i+1),
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
    '''
    Creates players and starts the game.
    '''
    def __init__(self, size):
        self.xo = ['X', 'O']
        self.s = State(size)
        self.size = size

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
        usr = UserPlayer(p1, p2, self.size)
        ai = AIPlayer(p2, p1, self.size)

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
    n = 3
    while True:
        print 'Enter number the size of the board: 3, 4 or 5'
        try:
            n = int(raw_input())
            if n not in [3, 4, 5]:
                raise ValueError
            break
        except ValueError as e:
            print "Choose either 3, 4 or 5."

    Game(n).play()
