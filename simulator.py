#Ian Miller
#simulator.py

from copy import deepcopy

class TwoPlayerSimulator(object):
    def __init__(self, controlStrategy, testStrategy):
        self.game = controlStrategy.game
        self.testStrategy = testStrategy
        self.controlStrategy = controlStrategy
        if self.testStrategy.game != self.controlStrategy.game:
            raise AttributeError("Same game must supply both strategies!")
        self.branches = []
        self.log = []
        self.logs = []
        self.winnersLog = []

    def simulate(self):
        self._generateBranches()
        for each in self.branches:
            each._takeTurn()
            if each.game.isOver:
                self.logs.append(each.log)
                self.winnersLog.append(each.game.winner)
            else:
                each.simulate()
                for log, winner in zip(each.logs, each.winnersLog):
                    self.logs.append(log)
                    self.winnersLog.append(winner)
        return

    def _generateBranches(self):
        self.controlStrategy.reanalyzeGameState()
        for each in self.controlStrategy.legalMoves:
            branch = deepcopy(self)
            branch.branches = []
            self.branches.append(branch)
            self.controlStrategy.nextBestMove()
        return

    def _takeTurn(self):
        if self.game.isOver:
            raise AttributeError("The game is over.")
        self.log.append(self.controlStrategy.bestMove)
        self.game.move(*self.controlStrategy.bestMove)
        if not self.game.isOver:
            self.log.append(self.testStrategy.bestMove)
            self.game.move(*self.testStrategy.bestMove)
        return

