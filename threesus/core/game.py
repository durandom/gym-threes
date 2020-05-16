from .deck import Deck
from .board import Board
from .card import Card
import numpy as np

class Game:
    deck = None
    board = None
    number_initial_cards = 9
    _next_card_id = 0

    def __init__(self):
        self._next_bonus_card = None

        self.deck = Deck()
        self.board = Board()

        self.initialize_board()

        print(self.board)


    def initialize_board(self):
        rng = np.random.default_rng()
        for i in range(self.number_initial_cards):
            while True:
                position = (rng.integers(self.board.height), rng.integers(self.board.width))
                if not self.board[position]:
                    self.board[position] = self.draw_next_card()
                    break

    def next_card_id(self):
        self._next_card_id = self._next_card_id + 1
        return self._next_card_id

    def draw_next_card(self):
        if self._next_bonus_card:
            card_value = self._next_bonus_card
        else:
            card_value = self.deck.draw_next_card()

        
        # Should the next card be a bonus card?
        max_card_value = self.board.get_max_card_value();
        # if(maxCardValue >= 48 && _rand.Single() < BONUS_CARD_CHANCE)
        # {
        #     List<int> possibleBonusCards = new List<int>(GetPossibleBonusCards(maxCardValue));
        #     _nextBonusCard = possibleBonusCards[_rand.Int32(0, possibleBonusCards.Count - 1)];
        # }
        # else
        # {
        #     _nextBonusCard = null;
        # }

        return Card(card_value, self.next_card_id())
    


