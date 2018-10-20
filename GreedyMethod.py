# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:43:51 2018

@author: hp

Greedy search
"""

import numpy as np
from PuzzleWorld import puzzle_world
from PuzzleNode import puzzle_node
from util import heuristic_func, check_list, delete_node, add_first_node, print_action_list

def Greedy(current_puzzle_node, goal_puzzle_node):

    open_list = []
    close_list = []
    move_action = ["right","left","up","down"]
    
    depth = 1
    DEPTH = 100
    open_list.append(current_puzzle_node)
    while (depth <= DEPTH): #step < 2: #
        exist_goal, ind = check_list(open_list, goal_puzzle_node) # 
        if exist_goal and ind==0: # greedy choosing the head node in open list
            goal_puzzle_node = open_list[ind]
            depth = goal_puzzle_node.g_value + 1
            break
        
        current_puzzle_node = open_list[0]
        open_list = delete_node(open_list, 0)
        
        close_list.append(current_puzzle_node)
        
        depth = current_puzzle_node.g_value + 1
        if depth == DEPTH:               
            ##########################################
            #print "Greedy reaching bottom" 
            ##########################################
            print(action_list(current_puzzle_node))
            print("No solution in greedy method before searching DEPTH {}".format(DEPTH))
            break
        
        available_node = [] # clear the history
        #print "## Iteration {}##".format(depth)
        #current_puzzle_node.puzzle.print_puzzle()
            
        # expand current_puzzle
        for action in move_action:
            #print "action {}".format(action)
            valid_action = False
            if action == "right":
                valid_action = current_puzzle_node.puzzle.move_right()
            elif action == "left":
                valid_action =  current_puzzle_node.puzzle.move_left()
            elif action == "up":
                valid_action =  current_puzzle_node.puzzle.move_up()
            else:
                valid_action =  current_puzzle_node.puzzle.move_down()
                
            if valid_action:
                new_puzzle = puzzle_world(3)
                new_puzzle.set_current_grid(current_puzzle_node.puzzle.return_update_grid())
                new_puzzle_node = puzzle_node(new_puzzle)
                
                new_puzzle_node.set_father_node(current_puzzle_node)
                new_puzzle_node.set_action(action)
                
                new_puzzle_node.set_h_value(heuristic_func(new_puzzle_node.puzzle, goal_puzzle_node.puzzle)) # cost from goal
                new_puzzle_node.set_g_value(current_puzzle_node.g_value + 1) # searching cost
                new_puzzle_node.set_f_value()
                
                available_node.append(new_puzzle_node)
                
                current_puzzle_node.puzzle.set_current_grid(current_puzzle_node.puzzle.current_grid) # reset update_grid in current_puzzle
        
                #print "reset current_puzzle_node"
                #current_puzzle_node.puzzle.print_puzzle()
            else:
                continue # action is not valid, continue to try other actions
          
        # find the node with minimum h_value
        # replace the current_node with this node
        min_value = np.inf
        flag = True
        for node in available_node:
            h_value = node.h_value 
            if h_value <= min_value: 
                min_value = h_value 
                exist_close, _ = check_list(close_list, node)
                if exist_close:
                    exist_node = node
                    continue
                else:
                    flag = False
                    add_first_node(open_list, node)
        
        # 这一层没有可以添加到close表的状态，即扩展的状态在之前都被访问过
        if flag:
            print_action_list(exist_node)
            print("At depth {}, greedy method sink in dead circle!".format(int(exist_node.g_value+1)))
            return False, len(close_list)
               
    if exist_goal:
        print("### find goal_puzzle in DFS with DEPTH {} ###".format(depth))
        print("### number of searching node in close_list {}".format(len(close_list)))
			    
        print_action_list(goal_puzzle_node)
        return True, len(close_list)
    # no solution if searching until MAXSTEP and goal not found
    else:
        print("No solution in greedy method before searching DEPTH {}".format(DEPTH))
        return False, len(close_list)
    