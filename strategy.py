#Ian Miller
#strategy.py

from abc import ABCMeta, abstractmethod

class Strategy(object):
    __metaclass__ = ABCMeta
    def __init__(self, game):
        self.game = game
        self.possibleMoves = []
        self.legalMoves = []

    @property
    def bestMove(self):
        pass

