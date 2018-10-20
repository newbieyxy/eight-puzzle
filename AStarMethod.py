# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:35:10 2018

@author: Xuyun Yang

A* searching method
"""

import numpy as np
from PuzzleWorld import puzzle_world
from PuzzleNode import puzzle_node
from util import heuristic_func, check_list, delete_node, print_action_list

def AStar(current_puzzle_node, goal_puzzle_node, h_mode):
    # expand_list = []
    open_list = []
    close_list = []
    move_action = ["right","left","up","down"]
    # if goal_puzzle_node is in open_list, then exist_goal = f_value of goal_puzzle; else exist_goal = False
    # print "check open_list at the beginning"
    
    # exist_goal, _ = check_list(open_list, goal_puzzle_node)
    # step = 1
    # MAXSTEP = 5
    depth = 1
    DEPTH = 50
    
    open_list.append(current_puzzle_node)
    while (len(open_list) > 0): #step < 2: #                
        # before next time expanding
        # check goal_puzzle is in open_list or not
        # print "check open_list to find goal"
        exist_goal, ind = check_list(open_list, goal_puzzle_node) # ind--the index of goal_puzzle_node in open_list
        if exist_goal:
            goal_puzzle_node = open_list[ind]
            depth = goal_puzzle_node.g_value + 1
            break
    
        # find the node in open_list w.r.t the best f_value 
        # return the current_puzzle prepared for close_list in the next iteration
        min_value = np.inf
        for node in open_list:
            value = node.f_value
            if value < min_value:
                min_value = value
                #current_puzzle = puzzle
                current_puzzle_node = node
        
        # delete the node (added in the close_list) in open_list
        _, ind = check_list(open_list, current_puzzle_node)
        open_list = delete_node(open_list, ind)

        #print "## Iteration {}##".format(depth)
        #print "current puzzle"
        close_list.append(current_puzzle_node)
        #current_puzzle_node.puzzle.print_puzzle()
        depth = current_puzzle_node.g_value + 1
        
        # reaching DEPTH, stop expanding
        if depth == DEPTH:                
            ##########################################
            #print "reaching bottom, visit neighbour" 
            ##########################################
            continue
            
        # expand current_puzzle
        for action in move_action:
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
                
                new_puzzle_node.set_h_value(heuristic_func(new_puzzle_node.puzzle, goal_puzzle_node.puzzle, h_mode)) # cost from goal
                new_puzzle_node.set_g_value(current_puzzle_node.g_value + 1) # searching cost
                new_puzzle_node.set_f_value()
                
                # new_puzzle_node.puzzle.print_puzzle()
                # print "check close_list to deal with new_puzzle_node"
                exist_close, _ = check_list(close_list, new_puzzle_node)
                if exist_close: 
                    #print "exist in close_list"
                    current_puzzle_node.puzzle.set_current_grid(current_puzzle_node.puzzle.current_grid) # reset update_grid in current_puzzle
                    continue
                else:
                    # print "check open_list to deal with new_puzzle_node"
                    f_old, list_ind = check_list(open_list, new_puzzle_node)
                    if f_old:
                        #print "exist in open_list"
                        f_new = new_puzzle_node.f_value
                        if f_new < f_old:
                            open_list[list_ind] = new_puzzle_node
                    else:
                        open_list.append(new_puzzle_node)
                
                current_puzzle_node.puzzle.set_current_grid(current_puzzle_node.puzzle.current_grid) # reset update_grid in current_puzzle
        
                #print "reset current_puzzle_node"
                #current_puzzle_node.puzzle.print_puzzle()
            else:
                continue # action is not valid, continue to try other actions
        
    if exist_goal:
        print("### find goal_puzzle in A* with DEPTH {} ###".format(int(depth)))
        print("### number of searching node in close_list {} ###".format(len(close_list)))
        print_action_list(goal_puzzle_node)
        return True, len(close_list)
    else:
        print("No solution in A* before searching DEPTH {}".format(DEPTH))
        return False, len(close_list)
    
    

