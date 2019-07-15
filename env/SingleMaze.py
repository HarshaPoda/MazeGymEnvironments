import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gym
from gym import error, spaces, utils

class newMaze(gym.Env):
    """A new Maze for the gym environment"""
    metadata = {'render.modes': ['human']}
    
    def __init__(self, m):
        super(newMaze, self).__init__()
        self.m = m
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Discrete(5)
        self.state = np.zeros(5) 
        self.agentPosition = 0
        self.numSteps = 0
        
    def step(self, action):
        
        if action == 0 and (self.agentPosition==0):
            self.agentPosition = self.agentPosition
            reward = -2      
        elif action == 0:
            self.agentPosition = self.agentPosition - 1
            reward = -1
            
        if action == 0:
            self.agentPosition = self.agentPosition
            reward = 0
        if action == 0:
            self.agentPosition = self.agentPosition + 1  
            reward = 1
        self.numSteps+=1
        if (self.agentPosition==4):
            done=True
        else:
            done=False
        return self.agentPosition,reward, done, None
    
    def reset(self):
        self.agentPosition = 0
        self.state = np.zeros(5)
        return self.agentPosition
    
    def render(self):
        print("Printing Board")
        for row in self.state:
            print('- ')
        
