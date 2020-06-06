from gym_threes.threes.core import Game
from gym_threes.threes.bots import RandomBot

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
