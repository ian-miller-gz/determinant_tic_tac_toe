#Ian Miller
#teststrategy.py

from simulator import TwoPlayerSimulator
from tictactoe import TicTacToe
from tictactoe_strategy import *

class TestStrategyTTO(StrategyTTO):
    def __init__(self, game):
        StrategyTTO.__init__(self, game)

    @property
    def bestMove(self):
        for each in self.game.cells:
            if TestStrategyTTO._isPriority(each):
                return self._parametizeCell(each)
        for each in self.game.cells:
            if TestStrategyTTO._isCandidate(each):
                return self._parametizeCell(each)
        for each in self.game.cells:
            if TestStrategyTTO._isOpen(each):
                return self._parametizeCell(each)
        raise LookupError(
            "{}: There are no candidate cells".format(self.game)
        )


    def _parametizeCell(self, cell):
        memberCandidate = None
        for each in cell.members:
            if each.holds == None:
                memberCandidate = each.label
        for each in cell.members:
            if each.holds == None and self._isThreatened(each.label):
                memberCandidate = each.label
        return (cell.num, memberCandidate)
        raise LookupError(
            "{0}, Cell #{1} has no open entries".format(self.game, cell.num)
        )

    def _isThreatened(self, cellNum):
        threat = False
        solution = False
        for each in self.game.cells[cellNum - 1].members:
            if each.holds == 1:
                threat = True
            if each.holds == 0:
                solution = True
        return threat and not solution
            

    @classmethod
    def _isPriority(cls, cell):
        oneCount = 0
        for each in cell.members:
            if each.holds == 1:
                oneCount += 1
            if each.holds == 0:
                return False
        return oneCount == len(cell.members) - 1

    @classmethod
    def _isCandidate(cls, cell):
        oneCount = 0
        for each in cell.members:
            if each.holds == 0:
                return False
            if each.holds == 1:
                oneCount += 1
        return (oneCount ==  1)

    @classmethod
    def _isOpen(cls, cell):
        for each in cell.members:
            if each.holds == None:
                return True
        return False


def run():
    players = ["PlayerOne", "PlayerTwo"]
    game = TicTacToe(players)
    conStrat = ControlStrategyTTO(game)
    tesStrat = TestStrategyTTO(game)
    simulation = TwoPlayerSimulator(conStrat, tesStrat)
    simulation.simulate()
    result = "PlayerOne" in [x.name for x in simulation.winnersLog]
    for log, winner in zip(simulation.logs, simulation.winnersLog):
        print(log, winner)
    print()
    print("PlayerOne in winners log: {}".format(result) )
    print("Number of games played: {}".format(len(set(simulation.winnersLog) ) ) )
    print("Goal number of games played: {}".format(9 * 7 * 5 * 3) )
    return


if __name__ == '__main__':
    run()
