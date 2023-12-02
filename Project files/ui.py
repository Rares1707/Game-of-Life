from board import Board
from texttable import Texttable

class Ui:
    def __init__(self, gameBoard: Board):
        self.board = gameBoard

    def displayTrueTable(self):
        table = Texttable()
        header = [i for i in range (1,9)]
        table.header(header)
        table.add_rows(self.board.data, False)
        print(table.draw())

    def startGame(self):
        self.displayTrueTable()
        while True:
            print("enter command")
            print()
            fullCommand = input().split(' ')
            try:
                if fullCommand[0] == 'exit':
                    return
                elif fullCommand[0] == 'save':
                    self.board.save(fullCommand[1].strip())
                elif fullCommand[0] == 'load':
                    self.board.load(fullCommand[1].strip())
                    self.displayTrueTable()
                elif fullCommand[0] == 'place':
                    self.board.placePattern(fullCommand[1], int(fullCommand[2]) - 1, int(fullCommand[3].strip()) - 1)
                    self.displayTrueTable()
                elif fullCommand[0] == 'tick':
                    try:
                        self.board.tick(int(fullCommand[1]))
                    except IndexError:
                        self.board.tick(1)
                    self.displayTrueTable()
            except Exception as error:
                print(error)
