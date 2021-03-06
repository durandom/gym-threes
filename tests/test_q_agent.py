import gym
import gym_threes.envs
import sys

import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

import keras
import numpy as np
import random
import matplotlib.pyplot as plt
from random import shuffle
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from collections import deque
import logging



class Agent():
    def __init__(self, obs_space, action_space):
        self.obs_space = obs_space
        self.action_space = action_space
        self.memory = deque(maxlen=10000)
        self.gamma = 0.99
        self.batch_size = 64
        self.model = self._build_model()

    def remember(self, observation, action, reward, next_observation):
        if len(self.memory) > self.memory.maxlen:
            if np.random.random() < 0.5:
                shuffle(self.memory)
            self.memory.popleft()
        self.memory.append((observation, action, reward, next_observation))

    def get_q(self, observation):
        np_obs = np.reshape(observation, [-1, self.obs_space])
        return self.model.predict(np_obs)

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, input_shape=(self.obs_space,), activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_space, activation='linear'))
        model.compile(optimizer=Adam(lr=0.001), loss='mse', metrics=[])
        return model

    def update_action(self, action_model, target_model):
        sample_transitions = random.sample(self.memory, self.batch_size)
        random.shuffle(sample_transitions)
        batch_observations = []
        batch_targets = []

        for old_observation, action, reward, observation in sample_transitions:
            # Reshape targets to output dimension(=2)
            targets = np.reshape(
                self.get_q(old_observation),
                self.action_space)
            targets[action] = reward  # Set Target Value
            if observation is not None:
                # If the old state is not a final state, also consider the
                # discounted future reward
                predictions = self.get_q(observation)
                new_action = np.argmax(predictions)
                targets[action] += self.gamma * predictions[0, new_action]

            # Add Old State to observations batch
            batch_observations.append(old_observation)
            batch_targets.append(targets)  # Add target to targets batch

        # Update the model using Observations and their corresponding Targets
        np_obs = np.reshape(batch_observations, [-1, self.obs_space])
        np_targets = np.reshape(batch_targets, [-1, self.action_space])
        self.model.fit(np_obs, np_targets, epochs=1, verbose=0)

    def save(self, path):
        self.model.save_weights(path)

    def load(self, path):
        self.model.load_weights(path)


def test_train():
    env = gym.make('Threes-v0')
    action_space = env.action_space.n
    observation_space = env.observation_space.shape[0]
    agent = Agent(observation_space, action_space)

    episodes = 20000  # Games played in training phase
    max_steps = 50000
    epsilon = 1
    epsilon_decay = 0.99
    epsilon_min = 0.05
    scores = [0]  # A list of all game scores
    recent_scores = []  # List that hold most recent 100 game scores
    mean_score = 0

    for episode in range(episodes):
        observation = env.reset()
        for iteration in range(max_steps):
            old_observation = observation

            if np.random.random() < epsilon:
                # Take random action (explore)
                action = np.random.choice(range(action_space))
            else:
                # Query the model and get Q-values for possible actions
                q_values = agent.get_q(observation)
                action = np.argmax(q_values)
            # Take the selected action and observe next state
            observation, reward, done, _ = env.step(action)
            if done:
                scores.append(reward)  # Append final score
                mean_score = np.mean(scores[-100:])
                # Calculate recent scores
                if len(scores) > 100:
                    recent_scores = scores[-100:]
                # Print end-of-game information
                print(
                    "\rEpisode {:03d} , epsilon = {:.4f}, moves = {:04d}, mean = {:05.1f}, score = {:05d}".format(
                        episode, epsilon, iteration, mean_score, reward), end="")
                sys.stdout.flush()
                # Add the observation to replay memory
                agent.remember(old_observation, action, reward, None)
                break
            # Add the observation to replay memory
            agent.remember(old_observation, action, reward, observation)
            # Update the Deep Q-Network Model (only with a chance of 25% and
            # when the last score was worse than 495)
            if len(agent.memory) >= agent.batch_size and np.random.random() < 0.25 and reward > mean_score:
                #print(f"retrain agent. reward {reward}, mean {mean_score}")
                agent.update_action(agent.model, agent.model)

        # If mean over the last 100 Games is >495, then success
        #if np.mean(recent_scores) > 495 and iteration > 495:
        #    print("\nEnvironment solved in {} episodes.".format(episode), end="")
        #    break
        epsilon = max(epsilon_min, epsilon_decay * epsilon)

    # Saving the model
    agent.model.save('models/threes_model.h5')

    # Plotting
    plt.plot(scores)
    plt.title('Training Phase')
    plt.ylabel('Score')
    plt.ylim(ymax=np.max(scores))
    plt.xlabel('Trial')
    plt.savefig('results/ThreesTraining.png', bbox_inches='tight')
    # plt.show()


def run_agent():
    env = gym.make("CartPole-v1")
    action_space = env.action_space.n
    observation_space = env.observation_space.shape[0]
    agent = Agent(observation_space, action_space)
    agent.load("models/cartpole_model.h5")
    scores = []

    # Playing 100 games
    for _ in range(100):
        obs = env.reset()
        episode_reward = 0
        while True:
            q_values = agent.get_q(obs)
            action = np.argmax(q_values)
            obs, reward, done, _ = env.step(action)
            episode_reward += reward
            if done:
                break
        scores.append(episode_reward)

    # Plot the Performance
    plt.plot(scores)
    plt.title('Testing Phase')
    plt.ylabel('Time Steps')
    plt.ylim(ymax=510)
    plt.xlabel('Trial')
    plt.savefig('results/CartPoleTesting.png', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    train()  # Train new weights
    test()  # Use existing weights to play
