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

    def shift(self, dir):
        self.temp_board.copy_from(self.board)
        new_card_cells = self.board.shift(dir)
        if new_card_cells:
            print("new cards at:")
            print(new_card_cells)
            for cell in new_card_cells:
                self.board[cell] = self.draw_next_card()
            self.prev_board.copy_from(self.temp_board)
            
        return bool(new_card_cells)

        
        # 	/// <summary>
        # /// Shifts the game board in the specified direction, merging cards where possible.
        # /// </summary>
        # /// <returns>Whether any cards were actually shifted.</returns>
        # public bool Shift(ShiftDirection dir)
        # {
        # 	_tempBoard.CopyFrom(_board);
        # 	List<IntVector2D> newCardCells = new List<IntVector2D>();
        # 	bool shifted = _board.Shift(dir, newCardCells);
        # 	if(shifted)
        # 	{
        # 		IntVector2D newCardCell = newCardCells[_rand.Int32(0, newCardCells.Count - 1)];
        # 		_board[newCardCell] = DrawNextCard();

        # 		_prevBoard.CopyFrom(_tempBoard);
        # 		LastShiftTime = DateTime.Now;
        # 		LastShiftDirection = dir;
        # 		TotalTurns++;
        # 	}
        # 	return shifted;
        # }

    


