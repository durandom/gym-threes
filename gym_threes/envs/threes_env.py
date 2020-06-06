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
    self.observation_space = spaces.Box(0, 2**squares, (self.w * self.h, ), dtype=np.int)
    # Guess that the maximum reward is also 2**squares though you'll probably never get that.
    self.reward_range = (0., float(2**squares))

    # Initialise seed
    self.seed()

    # Reset ready for a game
    self.reset()
    
    self.game = Game()

  def step(self, action):
    observation = "threes"
    reward = 0
    done = False
    info = dict()
    return observation, reward, done, info

  def reset(self):
    pass

  def render(self, mode='human'):
    pass

  def close(self):
    pass