from gym.envs.registration import register

register(
    id='Threes-v0',
    entry_point='gym_threes.envs:ThreesEnv'
)
