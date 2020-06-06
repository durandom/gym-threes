import random

class RandomBot(object):

    def __init__(self):
        self.valid_directions = []
        self.last_move = None

    def get_next_move(self, board, deck, next_card_hint, previous_shifted):
        if not previous_shifted and self.last_move:
            self.valid_directions.remove(self.last_move)
        else:
            self.update_valid_directions(board)

        if self.valid_directions:
            move = random.choice(self.valid_directions)
            self.last_move = move
            return move

        return None
    
    def update_valid_directions(self, board):
        self.valid_directions = board.all_shift_directions()


