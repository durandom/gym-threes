import random

class RandomBot(object):

    def __init__(self):
        pass

    def get_next_move(self, board, deck, next_card_hint):
        valid_directions = board.all_shift_directions()
        # return valid_directions[0]
        return random.choice(valid_directions)
