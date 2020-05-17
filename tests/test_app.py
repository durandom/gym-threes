from threesus.core import Game
from threesus.bots import RandomBot

def test_game():
    game = Game()
    bot = RandomBot()

    print("\n-------")
    print(game.board)

    while True:
        next_move = bot.get_next_move(game.board, game.deck, game.next_card_hint())
        print(f"shift {next_move}")

        if not next_move:
            break
        game.shift(next_move)

        print(game.board)

        break