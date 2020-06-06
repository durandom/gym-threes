from gym_threes.threes.core import Game
from gym_threes.threes.bots import RandomBot
from gym_threes.threes.core.card import Card

def test_game():
    game = Game()
    bot = RandomBot()
    shifted = False

    print("\nStart Board")
    print(f"{game.board}\n")

    while True:
        next_move = bot.get_next_move(game.board, game.deck, game.next_card_hint(), shifted)
        if not next_move:
            print(f"No more moves")
            break

        print(f"next_card hint {game.next_card_hint()}")
        print(f"shift {next_move}")
        shifted = game.shift(next_move)

        print(f"new Board:\n{game.board}\n")


def test_scores():
    assert Card(1, 1).score() == 0
    assert Card(2, 1).score() == 0
    assert Card(3, 1).score() == 3
    assert Card(6, 1).score() == 9
    assert Card(12, 1).score() == 27
    assert Card(384, 1).score() == 6561