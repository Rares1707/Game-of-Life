from unittest import TestCase
from board import Board

class Test_Board(TestCase):
    def setUp(self) -> None:
        self.board = Board('inexistentFile')
        self.board._data = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    def test_Tick1(self):
        expectedResult= [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', 'X', 'X', 'X', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.board.tick(1)
        TestCase.assertEqual(self, self.board._data, expectedResult)

    def test_Tick2(self):
            expectedResult = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            self.board.tick(4)
            TestCase.assertEqual(self, self.board._data, expectedResult)

