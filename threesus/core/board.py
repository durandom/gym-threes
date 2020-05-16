import numpy as np
from .card import Card

class Board():

    width = 4
    height = 4

    def __init__(self):
        self._board = np.empty([self.height, self.width], dtype=Card)

    def get_max_card_value(self):
        ret = 0
        for x in range(self.width):
            for y in range(self.height):
                card = self._board[(x, y)]
                if card:
                    if card.value > ret:
                        ret = card.value
        return ret

        
    def __getitem__(self, position):
        return self._board[position]
    
    def __setitem__(self, position, value):
        self._board[position] = value

    def __str__(self):
        return str(self._board)