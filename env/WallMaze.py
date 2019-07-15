import numpy as np
import pandas as pd
import maplotlib.pyplot as plt
import gym
from gym import error, spaces, utils

class MazeWorld(gym.Env):
    """ A maze with walls """
    metadata = { 'render.modes': ['human'] }
    
    def __init__(self, m, n, walls):
        super(MazeWorld, self).init__()
        self.grid = np.zeros((m,n))
        self.m = m
        self.n = n
        self.action_spaces = spaces.Discrete(4)
        self.observation_spaces = spaces.Box(0,1,(self.m*self.n,))
        self.agentPosition = 0
        self.addWalls(walls)
        self.terminalState = (self.m * self.n) - 1
        #self.state = (self.m * self.n)
        
    def addWalls(self,walls):
        self.walls = walls
        i = 0
        for i in walls:
            x = walls // self.n
            y = walls % self.n
            self.grid[x][y] = 1
    
    def getAgentRowAndColumn(self):
       x = self.agentPosition // self.n
       y = self.agentPosition % self.n
       return x,y
   
    def isTerminalState(self):
        if self.agentPosition == self.terminalState:
            return True
        else:
            return False
        
    def offGridMove(self, newState, oldState):
        
        #if newState in self.walls:
        #    return True
        
        # Checking for an illegal 'Left' move off the grid
        if (oldState % self.n == 0) and (newState % self.n == self.n - 1):       
            return True
        # Checking for an illegal 'Right' move off the grid
        elif (oldState % self.n == self.n - 1) and (newState % self.n == 0):
            return True
        # Checking for an illegal 'UP' move off the grid
        elif ( newState < 0):
            return True
        # Checking for an illegal 'Down' move off the grid
        elif (newState > (self.m*self.n) ) :
            return True
        else:
            return False
        
    def setState(self, tempState):
        x, y = self.getAgentRowAndColumn()
        self.grid[x][y] = 0
        self.agentPosition = tempState
        x, y = self.getAgentRowAndColumn()
        self.grid[x][y] = 2        
        
    def step(self, action):
        
        reward = 0
        tempState = 0
        if action == 0:
            tempState = self.agentPosition + self.n
        elif action == 1:
            tempState = self.agentPosition - self.n
        elif action == 2:
            tempState = self.agentPosition - 1
        elif action == 3:
            tempState = self.agentPosition + 1
      
        if tempState in walls:
            reward = -2
            #return self.agentPosition , reward, self.isTerminalState(), {}
        elif tempState == self.terminalState:
            reward = 0
        else:
            reward = -1
            
        if not self.offGridMove(tempState, self.agentPosition):
            self.setState(tempState)
            return tempState, reward, self.isTerminalState(), {}
        else:
            return self.agentPosition, reward, self.isTerminalState(), {}
        
    def reset(self):
        self.agentPosition = 0
        self.grid = np.zeros((self.m, self.n))
        self.addWalls(self.walls)
        return self.agentPosition
    
    def render(self):
        print("Printing board game")
        for row in self.grid:
            for col in row:
                if col == 1:
                    print( '|', end='\t')
                elif col == 2:
                    print( 'A', end='\t')
                else:
                    print( '-', end='\t')
            print('\n')
            
    
