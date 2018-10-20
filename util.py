# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:39:48 2018

@author: Xuyun Yang

Auxiliary function
"""

import numpy as np
from PuzzleWorld import puzzle_world
from PuzzleNode import puzzle_node

def generate_random_initial(world_shape, goal_puzzle_node):
    # indices = list(range(1, world_shape**2+1))
    # np.random.shuffle(indices)
    # grid = np.array(indices).reshape(world_shape,world_shape)

    initial_puzzle = puzzle_world(world_shape)
    initial_puzzle.set_current_grid(goal_puzzle_node.puzzle.current_grid)

    action = ["right", "left", "up", "down"]
    STEP = np.random.randint(20, 40)
    ind_last = 0
    step = 0
    while(step<=STEP):
        ind = np.random.randint(len(action))
        action_t = action[ind]
        if action_t == "right":
           valid_action = initial_puzzle.move_right()
        elif action_t == "left":
           valid_action = initial_puzzle.move_left()
        elif action_t == "up":
           valid_action = initial_puzzle.move_up()
        else:
           valid_action = initial_puzzle.move_down()

        if valid_action:
            if not (ind_last+ind==1 and ind_last+ind==5):
                initial_puzzle.set_current_grid(initial_puzzle.update_grid)
                #action_list.append(action_t)
                ind_last = ind
                step += 1
            else:
                initial_puzzle.set_current_grid(initial_puzzle.current_grid)

    initial_puzzle_node = puzzle_node(initial_puzzle)
    # set node value
    initial_puzzle_node.set_h_value(heuristic_func(initial_puzzle, goal_puzzle_node.puzzle))
    initial_puzzle_node.set_g_value(0.)
    initial_puzzle_node.set_f_value()

    return initial_puzzle_node


def heuristic_func(current_puzzle, goal_puzzle, method='manhattan'):
    h=0
    grid_pos = current_puzzle.grid_pos
    goal_grid_pos = goal_puzzle.grid_pos
    if method == 'manhattan':
        for i in range(len(grid_pos)-1):
            h += np.sum(abs(grid_pos[i]-goal_grid_pos[i]))
    elif method == 'misplacenum':
        for i in range(len(grid_pos)-1):
            if np.sum(abs(grid_pos[i]-goal_grid_pos[i]))!=0:
                h += 1
    else:
        raise NotImplementedError
    return h
    

def check_list(open_list, current_puzzle_node):
    if open_list == []:
        return False, None
    
    #print "node in check_list"
    #for node in open_list:
    #    node.puzzle.print_puzzle()
    #    print ""
    
    list_ind = 0
    for node in open_list:
        diff_sum = 0
        #for i in range(len(node.puzzle.grid_pos)-1):
        #    diff_sum += np.sum(abs(node.puzzle.grid_pos[i]-current_puzzle_node.puzzle.grid_pos[i]))
        diff_sum = np.sum(abs(node.puzzle.grid_pos-current_puzzle_node.puzzle.grid_pos))
        if diff_sum == 0:
            #print "check_list is true for"
            #current_puzzle_node.puzzle.print_puzzle()
            return node.f_value, list_ind # modified with returning f value
        list_ind += 1
    return False, None

# actually change the item of open_list in parameter list
def delete_node(close_list, ind):
    # for i in range(ind, len(close_list)-1):
    #    close_list[i] = close_list[i+1]
    del close_list[ind]
    return close_list

# actually change the item of open_list in parameter list
def add_first_node(open_list, new_node):
    open_list.insert(0, new_node)
    return open_list
    
def print_action_list(goal_puzzle_node):
    result_list = []
    result_list.append(goal_puzzle_node)
    current_node = goal_puzzle_node.father_node
    while current_node is not None:
        #print "result_list last puzzle"
        #result_list[-1].puzzle.print_puzzle() # will not print the start puzzle
        result_list.append(current_node)
        current_node = current_node.father_node
    
    action_list = []
    print("The solving process: ")
    for i in reversed(range(len(result_list))):
        state = result_list[i]
        if state.action is not None:
            action_list.append(state.action)
            #print state.action
        #state.puzzle.print_puzzle()
    print(action_list)
    return 
    


