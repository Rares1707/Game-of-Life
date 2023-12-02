from repo import Repository
from exceptions import BoardException

class Board:
    def __init__(self, repository: Repository):
        self.repository = repository
        self._dimensions = 8
        self._data = [[' ' for j in range(self.dimensions)] for i in range(self.dimensions)]

    def load(self, filename):
        starConfiguration = self.repository.getBoardConfiguration(filename)
        for x, y in starConfiguration:
            self._data[x][y] = 'X'  # magic letter

    def save(self, filename):
        coordinatesOfStars = []
        for x in range(8):  # magic numbers
            for y in range(8):
                if self._data[x][y] == 'X':
                    coordinatesOfStars.append([x, y])
        self.repository.saveBoardConfiguration(filename, coordinatesOfStars)

    def placePattern(self, patternName, cornerX, cornerY):
        newGrid = self._data
        pattern = self.repository.getPattern(patternName)
        for coordinates in pattern:
            if (cornerX + coordinates[0] < 8 and cornerY + coordinates[1] < 8 and
                    newGrid[cornerX + coordinates[0]][cornerY + coordinates[1]] == ' '):
                newGrid[cornerX + coordinates[0]][cornerY + coordinates[1]] = 'X'
            else:
                raise BoardException('Cannot place here')
        self._data = newGrid

    def _onBoard(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8


    def evolve(self):
        """
        Advances the simulation to the next generation, in accordance to the problem statement.
        :return: nothing, but the object's _data field will be replaced by the matrix representing the new generation
        """
        dx = [-1, 1, 1, 0, -1, 0, 1, -1]
        dy = [-1, 1, 0, 1, 0, -1, -1, 1]
        newGrid = [[' ' for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                liveNeighbours = 0
                for k in range(8):
                    xNeighbour, yNeighbour = i + dx[k], j + dy[k]
                    if self._onBoard(xNeighbour, yNeighbour):
                        if self._data[xNeighbour][yNeighbour] == 'X':
                            liveNeighbours += 1

                if self._data[i][j] == 'X':
                    if liveNeighbours < 2:
                        newGrid[i][j] = ' '
                    elif 2<= liveNeighbours <= 3:
                        newGrid[i][j] = 'X'
                    elif 3 < liveNeighbours:
                        newGrid[i][j] = ' '

                elif self.data[i][j] == ' ' and liveNeighbours == 3:
                    newGrid[i][j] = 'X'

        self._data = newGrid


    def tick(self, numberOfTicks):
        """
        calls the method evolve() multiple times in a recursive way
        :param numberOfTicks: the number of times we want to call the evolve() method
        """
        if numberOfTicks == 0:
            return
        else:
            self.evolve()
            self.tick(numberOfTicks-1)

    @property
    def data(self):
        return self._data

    @property
    def dimensions(self):
        return self._dimensions

