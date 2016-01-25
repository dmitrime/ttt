# -*- coding: utf-8 -*-


class Player(object):
    '''
    Base class.
    '''
    def __init__(self, xo, opponent):
        self.xo = xo
        self.opponent = opponent

    def makeMove(self, state):
        pass


class UserPlayer(Player):
    '''
    Human player.
    '''
    def __init__(self, xo, other):
        super(UserPlayer, self).__init__(xo, other)

    def makeMove(self, state):
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
