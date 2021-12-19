class Word:
    HORIZONTAL = 0
    VERTICAL = 1

    def __init__(self, word, x, y, direction):
        self.__word = word
        self.__xCoor = x
        self.__yCoor = y
        self.__direction = direction

    def getxCorr(self):
        return self.__xCoor
        
    def getyCorr(self):
        return self.__yCoor
    
    def getWordLength(self):
        return (len(self.__word))

    def getWordDirection(self):
        return (self.__direction)

    def getWord(self):
        return (self.__word)
