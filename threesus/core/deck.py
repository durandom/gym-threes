import numpy as np

class Deck:

    INITIAL_CARD_VALUES = [ 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3 ]

    def __init__(self):
        self.rebuild_deck()

    def draw_next_card(self):
        if (len(self.card_values) == 0):
            self.rebuild_deck()

        return self.card_values.pop()

    """
    Rebuilds the deck using a shuffled list of initial cards.
    Assumes that the deck is currently empty.
    """
    def rebuild_deck(self):
        # self.card_values = np.array(INITIAL_CARD_VALUES)
        self.card_values = list(self.INITIAL_CARD_VALUES)
        np.random.shuffle(self.card_values)

    