# -*- coding: utf-8 -*-
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
