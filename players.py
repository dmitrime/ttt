# -*- coding: utf-8 -*-
import operator


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


class AIPlayer(Player):
    '''
    Computer player.
    '''
    def __init__(self, xo, other):
        super(AIPlayer, self).__init__(xo, other)
        self.MAX_DEPTH = 6

    def evaluate(self, win, lose):
        '''
        Assign scores to a state given possible situations.
        '''
        if win:
            return 1
        elif lose:
            return -1
        else:
            return 0

    def minimax(self, depth, s, us, them):
        '''
        Simulate the game down to a given depth by switching players
        making their moves and both choosing the best ones.
        Each move is assined a score and the move with the best score is made.
        '''
        isFull, isWin, isLose = s.isBoardFull(), s.isWinning(self.xo), s.isWinning(self.opponent)
        if depth == 0 or isFull or isWin or isLose:
            return self.evaluate(isWin, isLose), None

        allMoves = [i for i in range(len(s.board)) if s.canPut(i)]

        if self.xo == us:
            topScore = float('-inf')
            condition = operator.gt
        else:
            topScore = float('inf')
            condition = operator.lt

        topPos = None
        for pos in allMoves:
            s.put(us, pos)
            score, _ = self.minimax(depth-1, s, them, us)
            #if depth == self.MAX_DEPTH:
                #print 'putting {} in {}: score = {}'.format(us, pos+1, score)
            s.unput(pos)
            if condition(score, topScore):
                topScore, topPos = score, pos
        return topScore, topPos

    def makeMove(self, state):
        print 'AI thinking...',
        _, pos = self.minimax(self.MAX_DEPTH, state, self.xo, self.opponent)
        print 'AI\'s move: {}'.format(pos+1)
        state.put(self.xo, pos)
        state.show()
