# -*- coding: utf-8 -*-
from player import Player


class AIPlayer(Player):
    '''
    Computer player.
    '''
    def __init__(self, xo, other, size):
        super(AIPlayer, self).__init__(xo, other, size)
        self.MAX_DEPTH = 10
        if size == 4:
            self.MAX_DEPTH = 7
        elif size == 5:
            self.MAX_DEPTH = 5
        self.WIN_SCORE = 7777777

    def evaluate(self, s, us, them):
        '''
        Assign scores to a state given possible situations.
        Count the number of our positions and their positions
        on each row, column and diagonal.
        '''
        score = 0
        lines = s.rows() + s.cols() + s.diag()
        for r in lines:
            a = r.count(us) * self.size
            b = r.count(them) * self.size
            if a > 0 and b == 0:
                score += a * self.size
            elif a == 0 and b > 0:
                score -= b * self.size
        return score

    def minimax(self, depth, s, us, them, alpha, beta):
        '''
        Simulate the game down to a given depth by switching players
        making their moves and both choosing the best ones.
        Each move is assined a score and the move with the best score is made.
        '''
        if s.isWinning(self.xo):
            return self.WIN_SCORE, None
        if s.isWinning(self.opponent):
            return -self.WIN_SCORE, None
        if depth == 0 or s.isBoardFull():
            return self.evaluate(s, us, them), None

        allMoves = [i for i in range(len(s.board)) if s.canPut(i)]

        topPos = None
        for pos in allMoves:
            s.put(us, pos)
            score, _ = self.minimax(depth-1, s, them, us, alpha, beta)
            #if depth == 1:
                #print score
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
