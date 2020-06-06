from .deck import Deck
from .board import Board
from .card import Card
import numpy as np
import random

class Game:
    deck = None
    board = None
    last_shift_direction = None
    total_turns = 0
    number_initial_cards = 9
    _next_card_id = 0
    _bonus_card_chance = 1 / 21

    def __init__(self):
        self._next_bonus_card = None

        self.deck = Deck()
        self.board = Board()

        self.initialize_board()

        self.prev_board = Board(self.board)
        self.temp_board = Board()


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

    def next_card_hint(self):
        next_card_value = self._next_bonus_card or self.deck.peek_next_card()
        return next_card_value

    def get_possible_bonus_cards(self, max_card_value):
        max_bonus_card = max_card_value / 8
        bonus_card = 6
        r = []
        while bonus_card <= max_bonus_card:
            r.append(bonus_card)
            bonus_card = bonus_card * 2

        return r

    def draw_next_card(self):
        if self._next_bonus_card:
            card_value = self._next_bonus_card
        else:
            card_value = self.deck.draw_next_card()

        # Should the next card be a bonus card?
        max_card_value = self.board.get_max_card_value();
        if max_card_value >= 48 and random.random() < self._bonus_card_chance:
            self._next_bonus_card = random.choice(self.get_possible_bonus_cards(max_card_value))
        else:
            self._next_bonus_card = None

        return Card(card_value, self.next_card_id())

    def shift(self, dir):
        self.temp_board.copy_from(self.board)
        new_card_cells = self.board.shift(dir)
        if new_card_cells:
            new_card_cell = random.choice(new_card_cells)
            print(f"new card at: {new_card_cell} - chosen from {new_card_cells}")
            self.board[new_card_cell] = self.draw_next_card()
            self.prev_board.copy_from(self.temp_board)
            self.last_shift_direction = dir
            self.total_turns = self.total_turns + 1
            
        return bool(new_card_cells)