class Cell:
    symbol = {
        0: ' ', 1: 'X', 2: '0'
    } 

    def __init__(self, number):
        self.number = number
        self.condition = False
        self.sym = self.symbol[0]
