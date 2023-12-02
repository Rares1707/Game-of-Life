from repo import Repository
from board import Board
from ui import Ui


repository = Repository('patterns.txt')
gameBoard = Board(repository)
gameUi = Ui(gameBoard)
gameUi.startGame()
