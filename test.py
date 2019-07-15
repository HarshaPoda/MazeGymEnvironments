import gym
import json
import datetime as dt

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2

from env.WallMaze import MazeWorld

import pandas as pd
#walls = {2, 4, 8, 10}
#walls = [2,4,8,10]
#env = DummyVecEnv([lambda: TestWorld(3,5,walls)])
#env = DummyVecEnv([lambda: newMaze(5)])
env = DummyVecEnv( [lambda: MazeWorld(3,4)])
model = PPO2(MlpPolicy, env, verbose=1).learn(total_timesteps=20000)
#model.learn(total_timesteps=20000)

obs = env.reset()
for i in range(2000):
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()
