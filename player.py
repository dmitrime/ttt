# -*- coding: utf-8 -*-


class Player(object):
    '''
    Base class.
    '''
    def __init__(self, xo, opponent, size):
        self.xo = xo
        self.opponent = opponent
        self.size = size

    def makeMove(self, state):
        pass


class UserPlayer(Player):
    '''
    Human player.
    '''
    def __init__(self, xo, other, size):
        super(UserPlayer, self).__init__(xo, other, size)

    def makeMove(self, state):
        nn = self.size*self.size
        while True:
            print 'Enter number where to put \'{}\' [1..{}]'.format(self.xo, nn)
            try:
                pos = int(raw_input())
                if pos < 1 or pos > nn:
                    raise ValueError("Choose position in range [1..{}]!".format(nn))
                state.put(self.xo, pos-1)
                break
            except ValueError as e:
                if e.message.startswith('invalid literal'):
                    print "Type a number in range [1..{}]!".format(nn)
                else:
                    print e
                continue
        state.show()
