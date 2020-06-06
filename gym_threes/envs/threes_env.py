import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
from gym_threes.threes.core import Game


class ThreesEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # Definitions for game. Board must be square.
        self.size = 4
        self.w = self.size
        self.h = self.size
        squares = self.size * self.size

        # Maintain own idea of game score, separate from rewards
        self.score = 0

        # Members for gym implementation
        self.action_space = spaces.Discrete(4)
        # Suppose that the maximum tile is as if you have powers of 2 across the board.
        self.observation_space = spaces.Box(
            0, 2**squares, (self.w * self.h, ), dtype=np.int)
        # Guess that the maximum reward is also 2**squares though you'll probably never get that.
        self.reward_range = (0., float(2**squares))

        # Initialise seed
        self.seed()

        self.game = Game()
        self.all_shift_directions = self.game.board.all_shift_directions()

        # Reset ready for a game
        self.reset()

    def step(self, action):
        self.game.shift(self.all_shift_directions[action])
        observation = 0
        reward = self.game.score()
        done = False
        info = {'board': self.game.board}
        return observation, reward, done, info

    def reset(self):
        self.game.reset()

    def render(self, mode='human'):
        print(self.game.board)

    def close(self):
        pass
