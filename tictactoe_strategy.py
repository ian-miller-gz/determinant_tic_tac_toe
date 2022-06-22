from game import Game
from strategy import Strategy
from tictactoe import *
from copy import deepcopy


class StrategyTTO(Strategy):
    _gameType = TicTacToe
    def __init__(self, game):
        Strategy.__init__(self, game)
        self._init_possibleMoves()
        self._init_legalMoves()

    def _init_possibleMoves(self):
        cells = [each.num for each in self.game.cells]
        midpoint = len(cells) // 2
        for each in cells[:midpoint]:
            for other in cells[midpoint:]:
                move = (each, other)                
                self.possibleMoves.append( (each, other) )
        return

    def _init_legalMoves(self):
        self.legalMoves = []
        branch = deepcopy(self.game)
        for each in self.possibleMoves:
            try:
                branch.move(*each)
            except ValueError:
                continue
            else:
                self.legalMoves.append(each)
        return


class ControlStrategyTTO(StrategyTTO):
    def __init__(self, game):
        StrategyTTO.__init__(self, game)
        self._iteration = 0
        
    @property
    def bestMove(self):
        try:
            return self.legalMoves[self._iteration]
        except IndexError:
            raise IndexError("All legal moves have been iterated through!")

    def reanalyzeGameState(self):
        self._iteration = 0
        self._init_legalMoves()

    def nextBestMove(self):
        self._iteration += 1

    def _init_legalMoves(self):
        StrategyTTO._init_legalMoves(self)
