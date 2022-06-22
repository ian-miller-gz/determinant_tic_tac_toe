#Ian Miller
#game.py

from abc import ABCMeta, abstractmethod


class Turn(object):
    def __init__(self, number, player):
        self.number = number
        self.player = player
        self.skip = False

    def __str__(self):
        if self.skip:
            skipMsg = "skipped"
        else:
            skipMsg = ""
        return "{0}: {1} {2}".format(self.number, self.player, skipMsg)


class Game(object):
    __metaclass__ = ABCMeta
    rules = ""
    def __init__(self, players):
        self._init_turnOrder(players)
        self._currentTurn = 0
        self.winner = None        

    @property
    @abstractmethod
    def isOver(self):
        pass

    @property
    def turn(self):
        return self._turnOrder[self._currentTurn]

    def _init_turnOrder(self, players):
        self._turnOrder = [Turn(number, player) for (number,player) in 
            zip([x for x in range(1, len(players) + 1)], players)
        ]
        return

    def endTurn(self, skipCount=0):
        lastTurn = self.turn.number
        self._currentTurn += 1
        self._currentTurn %= len(self._turnOrder)
        self.turn.number = lastTurn + 1
        return
