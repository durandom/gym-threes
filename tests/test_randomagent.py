import gym
import gym.spaces
import gym_threes.envs
import numpy as np
import random


def test_randomagent(verbose=True):
    # Initializing the list of scores
    scores = []
    
    # Creating the gym environment
    env = gym.make("Threes-v0")

    # Amount of games the agent plays
    episodes = 5

    # Maximum steps the agent has per episode
    max_steps = 100

    for episode in range(episodes):
        # Reset the state, done and score before every episode
        env.reset()
        done = False
        score = 0

        for _ in range(max_steps):
            # Act randomly until done or maximum steps reached
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            score = reward
            # print(info['board'])
            if done:
                break
        
        scores.append(score)
        if verbose:
            print("Episode: {}/{}, score: {}".format(episode+1, episodes, score))

    return scores


if __name__ == "__main__":
    randomagent(verbose=True)
