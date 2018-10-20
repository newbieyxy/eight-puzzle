# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:37:56 2018

@author: Xuyun Yang

Puzzle node
"""

class puzzle_node(object):
    def __init__(self, new_puzzle):
        self.puzzle = new_puzzle
        self.father_node = None
        self.action = None # the action reaching this node
        self.h_value = 0
        self.g_value = 0 # searching depth
        self.f_value = 0
        
    def set_h_value(self, h_value):
        self.h_value = h_value
        return
        
    def set_g_value(self, steps):
        self.g_value = steps
        return
                
    def set_f_value(self):
        # f = g+h
        self.f_value = self.g_value + self.h_value
        return
    
    def set_father_node(self, last_puzzle_node):
        self.father_node = last_puzzle_node
        
    def set_action(self, action):
        self.action = action
        
