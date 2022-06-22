#Ian Miller
#tictactoe.py

from abc import ABCMeta, abstractmethod
from game import Game, Turn


class Player(object):
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __str__(self):
        return "{0}({1})".format(self.name, self.mark)


class Entry(object):
    def __init__(self, label):
        self.label = label
        self.holds = None

    def assign(self, value):
        self.holds = value

    def unassign(self):
        self.holds = None


class Cell(object):
    _numCells = 6 
    _halfCells = 3
    _entryType = Entry
    def __init__(self, num):
        self.num = num
        self._init_members_() #Requires self.num
        return    

    def evaluate(self):
        result = 1 #assign to 1 since we are finding the product
        for each in self.members:
            result *= each.holds
        if self.num > Cell._halfCells:
            result *= -1
        return result

    def _init_members_(self):
        if self.num > 0 and self.num <= Cell._halfCells:
            self.members = [Cell._entryType(x) for x in 
                range(Cell._halfCells + 1, Cell._numCells + 1)]
        elif self.num >= Cell._halfCells and self.num <= Cell._numCells:
            self.members = [Cell._entryType(x) for x in 
                range(1, Cell._halfCells + 1)]
        else:
            self.members = None
            raise AttributeError(
                "Cell must be from {0} to {1}".format(1, Cell._numCells)
            )

    def __repr__(self):
        return "{0}, {1}, {2}" .format(self.members[0].holds, self.members[1].holds, self.members[2].holds)


class TicTacToe(Game):
    rules = "Determinant Tic-Tac-Toe"
    _cellType = Cell
    _lastTurn = _cellType._halfCells * _cellType._halfCells
    _playerCount = 2
    def __init__(self, playerNames = ["PlayerOne", "PlayerTwo"]):
        Game.__init__(self, playerNames)
        self._init_turnOrder_(playerNames)
        self._init_cells_()

    @property
    def isOver(self):
        if self.turn.number > TicTacToe._lastTurn:
            return True
        else: 
            return False

    @classmethod
    def _objectifyPlayers(cls, playerNames):
        playerObjs = [Player(each, x) for (each, x) in 
            zip(playerNames, reversed(range(0, TicTacToe._playerCount) ) )]
        return playerObjs

    def move(self, rightCell, leftCell):
        self._placeMark(rightCell, leftCell)
        self._placeMark(leftCell, rightCell)
        self.endTurn()
        if self.isOver:
            self._determineWinner()

    def _init_turnOrder_(self, playerNames):
        playerObjs = TicTacToe._objectifyPlayers(playerNames)
        for turn, player in zip(self._turnOrder, playerObjs):
            turn.player = player
        
    def _init_cells_(self):
        self.cells = [TicTacToe._cellType(i) for i in 
            range(1, TicTacToe._cellType._numCells + 1)]

    def _determineWinner(self):
        winnersMark = 0
        for each in self.cells:
            winnersMark += each.evaluate()
        winnersMark = abs(winnersMark)
        playerMarks = [each.player.mark for each in self._turnOrder]
        winnersIndex = playerMarks.index(winnersMark)
        self.winner = self._turnOrder[winnersIndex].player

    def _placeMark(self, numCell, numMember):
        cell = self.cells[numCell - 1]
        labels = [each.label for each in cell.members]
        if not numMember in labels:
            raise LookupError(
                "{0} is not a member of cell{1}".format(cell.num, numCell)
            )
        entry = cell.members[labels.index(numMember)]
        if entry.holds != None:
            raise ValueError(
                "Cell: {0}, {1} is already marked!".format(cell.num,entry.label)
            )
        entry.holds = self.turn.player.mark
