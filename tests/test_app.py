from threesus.core import Game
from threesus.bots import RandomBot

def test_game():
    game = Game()
    bot = RandomBot()

    while True:
        next_move = bot.get_next_move(game.board, game.deck, game.next_card_hint())

        if not next_move:
            break
        game.shift(next_move)
        print(game.board)
        break