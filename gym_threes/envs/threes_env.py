import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
from gym_threes.threes.core import Game
from six import StringIO
import logging


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
        dir = self.all_shift_directions[action]
        logging.debug(f"shifting {dir}")
        shifted = self.game.shift(dir)
        if shifted:
          self.avail_shift_directions = self.all_shift_directions.copy()
          reward = self.game.score()
        else:
          reward = 0 
          if dir in self.avail_shift_directions:
            self.avail_shift_directions.remove(dir)

        observation = self.state()
        if len(self.avail_shift_directions) == 0:
            done = True
            reward = self.game.score()
        else:
            done = False

        info = {'board': self.game.board}
        return observation, reward, done, info

    def reset(self):
        self.game.reset()
        self.avail_shift_directions = self.all_shift_directions.copy()
        return self.state()

    def render(self, mode='human'):
        outfile = StringIO() if mode == 'ansi' else sys.stdout
        s = 'Score: {}\n'.format(self.game.score)
        s += 'Highest: {}\n'.format(self.highest())
        npa = np.array(self.Matrix)
        grid = npa.reshape((self.size, self.size))
        s += "{}\n".format(grid)
        outfile.write(s)
        return outfile
        print(self.game.board)

    def close(self):
        pass

    def state(self):
      return self.game.board._board.flatten().astype(int)
