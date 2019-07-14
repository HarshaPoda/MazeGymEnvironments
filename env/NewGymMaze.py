#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 15:45:56 2019

@author: harshapodapati
"""

import numpy as np
import matplotlib.pyplot as plt

class TestWorld(object):
    def __init__(self, m, n, walls):
        self.grid = np.zeros((m,n))
        self.m = m
        self.n = n
        self.State_Space = [i for i in range(self.m*self.n)]
        self.State_Space.remove(self.m*self.n-1)
        self.State_Space_Plus = [ i for i in range(self.m*self.n)]
        
        self.action_space = {'U' : -self.n, 'D' : self.n, 
                            'L' : -1, 'R' : 1}
        self.possibleActions = ['U', 'D', 'L', 'R']
        self.agentPosition = 0
        self.addWalls(walls)
        
    def addWalls(self, walls):
        self.walls = walls
        i = 0
        for wall in walls:
            x = wall // self.n
            y = wall % self.n
            self.grid[x][y] = 1    
            
    def getAgentRowAndColumn(self):
        x = self.agentPosition // self.n
        y = self.agentPosition % self.n
        return x,y
    
    def setState(self, state):
        x, y = self.getAgentRowAndColumn()
        self.grid[x][y] = 0
        self.agentPosition = state
        x, y = self.getAgentRowAndColumn()
        self.grid[x][y] = 2
    
    def offGridMove(self, newState, oldState):
        if newState not in self.State_Space_Plus:
            return True
        elif oldState % self.m == 0 and newState % self.m == self.m -1:
            return True
        elif oldState % self.m == self.m - 1 and newState % self.m == 0:
            return True
        else:
            return False            
        
    def isTerminalState(self, state):
        return state in self.State_Space_Plus and state not in self.State_Space
    
    def actionSpaceSample(self):
        return np.random.choice(self.possibleActions)
        
    def reset(self):
        self.agentPosition = 0
        self.grid = np.zeros((self.m, self.n))
        self.addWalls(self.walls)
        return self.agentPosition
    
    def step(self, action):
        x, y = self.getAgentRowAndColumn()
        AgentState = self.agentPosition
        tempState = self.agentPosition + self.action_space[action]
        #print("This is resulting State" , tempState)
        #while tempState in self.walls:
        #    tempState = AgentState
        #    tempState = self.agentPosition + self.action_space[np.random.choice(self.possibleActions)]
        """while (tempState in self.walls) or (self.offGridMove(tempState, self.agentPosition)):
            tempState = AgentState
            tempState = self.agentPosition + self.action_space[np.random.choice(self.possibleActions)]
            
            print("testing State" , tempState)
            
            if tempState in self.walls:
                print("In an error state")
            elif not self.offGridMove(tempState, self.agentPosition):
                print(" Valid Move ")
            else:
                print(" Not valid move ")
            """

        #reward = -1 if not self.isTerminalState(tempState) else 0
        if tempState in walls:
            reward = -2
        elif not self.isTerminalState(tempState):
            reward = -1
        else:
            reward = 0
        
        if not self.offGridMove(tempState, self.agentPosition):
            self.setState(tempState)
            return tempState, reward, self.isTerminalState(self.agentPosition), None
        else:
            return self.agentPosition, reward, self.isTerminalState(self.agentPosition), None
        
    def render(self):
        print("Printing board game")
        for row in self.grid:
            for col in row:
                if col == 1:
                    print( '|', end='\t')
                else:
                    print( '-', end='\t')
            print('\n')
