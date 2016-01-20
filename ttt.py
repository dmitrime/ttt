import copy
import random


class State:
    '''
    Holds the state of the game.
    '''
    def __init__(self):
        self.board = self._empty_board()

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

    def isWinning(self, player):
        '''
        Checks if "player" has won.
        '''
        win = [player]*3
        rows = [self.board[:3], self.board[3:6], self.board[6:]]
        cols = self._cols(self.board)
        diag = self._diag(self.board)
        for x in rows+cols+diag:
            if win == x:
                return True
        return False

    def isGameOver(self):
        return all(self.board)

    def show(self):
        for i in range(len(self.board)):
            if i % 3 == 0:
                print
            print '{} '.format(self.board[i] if self.board[i] else i+1),
        print '\n'

    def put(self, xo, i):
        if self.board[i] is not None:
            raise ValueError("Choose an empty square!")
        self.board[i] = xo

    def copy(self):
        return copy.deepcopy(self)


class Player(object):
    def __init__(self, xo):
        self.xo = xo

    def makeMove(self, state):
        pass


class UserPlayer(Player):
    def __init__(self, xo):
        super(UserPlayer, self).__init__(xo)

    def makeMove(self, state):
        state.show()
        while True:
            print 'Enter number where to put \'{}\' [1..9]'.format(self.xo)
            try:
                pos = int(raw_input())
                if pos < 1 or pos > 9:
                    raise ValueError("Choose position in range [1..9]!")
                state.put(self.xo, pos-1)
                break
            except ValueError as e:
                if e.message.startswith('invalid literal'):
                    print "Type a number in range [1..9]!"
                else:
                    print e
                continue
        state.show()


class AIPlayer(Player):
    def __init__(self, xo):
        super(AIPlayer, self).__init__(xo)

    def makeMove(self, state):
        print 'AI thinking...',
        print 'AI\'s move: '


def start(s, xo):
    print 'New game'
    p = random.randint(0, 1)
    usr = UserPlayer(xo[p])
    ai = AIPlayer(xo[1-p])

    if usr.xo == xo[0]:
        print 'User starts the game with \'{}\''.format(xo[0])
        usr.makeMove(s)
    else:
        print 'AI starts the game with \'{}\''.format(xo[0])

    while not s.isGameOver():
        ai.makeMove(s)
        usr.makeMove(s)

    if s.isWinning(usr.xo):
        print 'You\'ve won, impressive!'
    elif s.isWinning(ai.xo):
        print 'You lose, sorry...'
    else:
        print 'It\'s a draw.'


if __name__ == '__main__':
    s = State()
    s.board = [None, 'O', 'X', None, 'X', 'O', 'X', 'O', 'X']
    #s.show()
    #print s.isWinning('X')

    start(State(), ['X', 'O'])