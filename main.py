import gym
import json
import datetime as dt

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2

from env.SingleMaze import NewMaze

import pandas as pd
walls = {2, 5, 12, 13}
#env = DummyVecEnv([lambda: TestWorld(3,5,walls)])
env = DummyVecEnv([lambda: newMaze(5)])
model = PPO2(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=20000)

obs = env.reset()
for i in range(2000):
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()
