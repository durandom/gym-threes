import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
from gym_threes.threes.core import Game


class ThreesEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.width = 4
        self.height = 4
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box( 0, 6144, (self.width * self.height, ), dtype=np.int)
        self.game = Game()
        self.all_shift_directions = self.game.board.all_shift_directions()

        # Reset ready for a game
        self.reset()

    def step(self, action):
        self.game.shift(self.all_shift_directions[action])
        observation = self.game.board._board.flatten()
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
