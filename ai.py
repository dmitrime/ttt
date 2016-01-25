# -*- coding: utf-8 -*-
import operator
from player import Player


class AIPlayer(Player):
    '''
    Computer player.
    '''
    def __init__(self, xo, other):
        super(AIPlayer, self).__init__(xo, other)
        self.MAX_DEPTH = 10

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

    def minimax(self, depth, s, us, them, alpha, beta):
        '''
        Simulate the game down to a given depth by switching players
        making their moves and both choosing the best ones.
        Each move is assined a score and the move with the best score is made.
        '''
        isFull, isWin, isLose = s.isBoardFull(), s.isWinning(self.xo), s.isWinning(self.opponent)
        if depth == 0 or isFull or isWin or isLose:
            return self.evaluate(isWin, isLose), None

        allMoves = [i for i in range(len(s.board)) if s.canPut(i)]

        topPos = None
        for pos in allMoves:
            s.put(us, pos)
            score, _ = self.minimax(depth-1, s, them, us, alpha, beta)
            s.unput(pos)

            if self.xo == us and score > alpha:
                alpha, topPos = score, pos
            elif self.xo != us and score < beta:
                beta, topPos = score, pos

            if alpha >= beta:
                break

        return alpha if self.xo == us else beta, topPos

    def makeMove(self, state):
        print 'AI thinking...',
        _, pos = self.minimax(self.MAX_DEPTH,
                              state,
                              self.xo,
                              self.opponent,
                              float('-inf'),
                              float('inf'))
        print 'AI\'s move: {}'.format(pos+1)
        state.put(self.xo, pos)
        state.show()
