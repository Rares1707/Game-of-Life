

class Repository:
    def __init__(self, patternsFileName):
        self._patternsFileName = patternsFileName

    def getBoardConfiguration(self, filename):
        coordinatesOfStars = []
        inputFile = open(filename, 'r')
        for line in inputFile.readlines():
            x, y = line.split(' ')
            coordinatesOfStars.append([int(x), int(y.strip())])
        inputFile.close()
        return coordinatesOfStars

    def saveBoardConfiguration(self, filename, coordinatesOfStars):
        outputFile = open(filename, 'w')
        for x, y in coordinatesOfStars:
            outputFile.write(str(x) + ' ' + str(y) + '\n')
        outputFile.close()

    def getCoordinates(self, inputFile):
        coordinatesOfStars = []
        tuples = inputFile.readline().strip().split(',')
        for tuple in tuples:
            x, y = tuple.split(' ')
            coordinatesOfStars.append([int(x), int(y)])
        return coordinatesOfStars

    def getPattern(self, patternName):
        inputFile = open(self._patternsFileName, 'r')
        pattern = {'block': self.getCoordinates(inputFile), 'tub': self.getCoordinates(inputFile),
                   'blinker': self.getCoordinates(inputFile), 'beacon': self.getCoordinates(inputFile),
                   'spaceship': self.getCoordinates(inputFile)}
        inputFile.close()
        return pattern[patternName]


