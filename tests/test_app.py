from threesus.core import Game
from threesus.bots import RandomBot

def test_game():
    game = Game()
    bot = RandomBot()

    print("\nStart Board")
    print(f"{game.board}\n")

    while True:
        next_move = bot.get_next_move(game.board, game.deck, game.next_card_hint())
        print(f"shift {next_move}")

        if not next_move:
            break
        shifted = game.shift(next_move)

        if not shifted:
            break

        print(f"new Board:\n{game.board}\n")
