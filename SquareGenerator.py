import random as ran

class RandomSquare():
    numToFile = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}

    def __init__(self):
        rank = 0
        file = 0

    def generate(self):
        return ran.randint(1,8)

    def generateSquare(self):
        row = self.generate()
        file = self.numToFile[self.generate()]
        square = file + str(row)
        return square

