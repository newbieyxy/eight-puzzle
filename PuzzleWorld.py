# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:28:58 2018

@author: Xuyun Yang

Eight puzzles world.
"""

import numpy as np

class puzzle_world(object):
    def __init__(self, world_shape):
        self.world_shape = world_shape
        self.puzzles_num = self.world_shape**2
        
         # puzzle_world state (for record, current--updated--goal)
        self.current_grid = np.zeros((3,3))
        self.update_grid = self.current_grid.copy()
        #self.goal_grid = np.zeros((3,3))
        #self.goal_grid = np.array(range(1,self.puzzles_num+1)).reshape(self.world_shape, self.world_shape)
        
        # puzzle_world info (for cal heuristic)
        self.grid_pos = np.zeros((self.puzzles_num, 2)) # storing the grid position of each puzzles
        self.update_grid_pos = self.grid_pos.copy()
        self.empty_pos = np.array((0,0)) # storing the grid position of empty puzzles
        self.update_empty_pos = self.empty_pos.copy()
        
        #self.goal_grid_pos = np.zeros((self.puzzles_num, 2))
        #for i in range(self.puzzles_num):
        #    self.goal_grid_pos[i] = np.argwhere(self.goal_grid == i+1)[0]

    ###############
    # env setting
    ###############
    
    # random initial
    def reset(self):
        indices = range(1,self.puzzles_num+1)
        np.random.shuffle(indices)
        self.current_grid = np.array(indices).reshape(3,3)
        for i in range(self.puzzles_num):
            self.grid_pos[i] = np.argwhere(self.current_grid == i+1)[0]
        self.empty_pos = np.argwhere(self.current_grid == 9)[0]
        
        self.update_grid = self.current_grid.copy()
        self.update_grid_pos = self.grid_pos.copy()
        self.update_empty_pos = self.empty_pos.copy()
        
        #print self.current_grid
        return
        
    # specific initial
    def set_current_grid(self, update_grid):
       self.current_grid = update_grid
       for i in range(self.puzzles_num):
           #print "update_grid {}".format(self.current_grid)
           self.grid_pos[i] = np.argwhere(self.current_grid == i+1)[0]
       self.empty_pos = np.argwhere(self.current_grid == 9)[0]
       
       self.update_grid = self.current_grid.copy()
       self.update_grid_pos = self.grid_pos.copy()
       self.update_empty_pos = self.empty_pos.copy()
       return
    
    ###############
    # env action
    ###############
    def move_right(self):
        if self.empty_pos[1]<=0:
            #raise Exception ("Moving right is not available, the empty grid is on the left side!")
            return False
        self.update_grid[self.empty_pos[0]][self.empty_pos[1]] = self.update_grid[self.empty_pos[0]][self.empty_pos[1]-1]       
        self.update_grid[self.empty_pos[0]][self.empty_pos[1]-1] = 9 
        #print "[in move_right]"
        for i in range(self.puzzles_num):
            self.update_grid_pos[i] = np.argwhere(self.update_grid == i+1)[0]
        self.update_empty_pos[1] -= 1
        return True
    
    def move_left(self):
        if self.empty_pos[1]>=self.world_shape-1:
            #raise Exception ("Moving left is not available, the empty grid is on the right side!")
            return False
        self.update_grid[self.empty_pos[0]][self.empty_pos[1]] = self.update_grid[self.empty_pos[0]][self.empty_pos[1]+1]
        self.update_grid[self.empty_pos[0]][self.empty_pos[1]+1] = 9
        #print "[in move_left]"
        for i in range(self.puzzles_num):
            self.update_grid_pos[i] = np.argwhere(self.update_grid == i+1)[0]
        self.update_empty_pos[1] += 1
        return True
    
    def move_up(self):
        if self.empty_pos[0]>=self.world_shape-1:
           #raise Exception ("Moving up is not available, the empty grid is on the top!")
           return False
        self.update_grid[self.empty_pos[0]][self.empty_pos[1]] = self.update_grid[self.empty_pos[0]+1][self.empty_pos[1]]
        self.update_grid[self.empty_pos[0]+1][self.empty_pos[1]] = 9
        #print "[in move_up]"
        for i in range(self.puzzles_num):
            self.update_grid_pos[i] = np.argwhere(self.update_grid == i+1)[0]
        self.update_empty_pos[0] += 1
        return True
    
    def move_down(self):
        if self.empty_pos[0]<=0:
            #raise Exception ("Moving up is not available, the empty grid is at the bottom!")
            return False
        self.update_grid[self.empty_pos[0]][self.empty_pos[1]] = self.update_grid[self.empty_pos[0]-1][self.empty_pos[1]]
        self.update_grid[self.empty_pos[0]-1][self.empty_pos[1]] = 9
        for i in range(self.puzzles_num):
            self.update_grid_pos[i] = np.argwhere(self.update_grid == i+1)[0]
        self.update_empty_pos[0] -= 1
        return True
    
    ###############
    # env status
    ###############
    def return_current_world(self):
        return self.current_grid
    
    def return_update_grid(self):
        return self.update_grid
    
    #def return_goal_world(self):
    #    return self.goal_grid
    
        
    ###############
    # env auxilary
    ###############
    def print_puzzle(self):
        for i in range(self.world_shape):
            item = []
            for j in range(self.world_shape):
                if self.current_grid[i][j] == 9:
                    item.append(' ')
                else:
                    item.append(str(self.current_grid[i][j]))
            print(item)
        return
        
    
    