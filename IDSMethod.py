# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:43:51 2018

@author: hp

Iterative deepening search
"""

import numpy as np
from PuzzleWorld import puzzle_world
from PuzzleNode import puzzle_node
from util import heuristic_func, check_list, delete_node, add_first_node, print_action_list


def IDS(start_puzzle_node, goal_puzzle_node):
    current_puzzle_node = start_puzzle_node
    MAXDEPTH = 15
    DEPTH = 1 # max searching depth for one dfs iteration
    close_list_sum = 0
    move_action = ["right","left","up","down"]
    # exist_goal = (current_puzzle_node.puzzle.current_grid == goal_puzzle_node.puzzle.current_grid).all()
    while DEPTH <= MAXDEPTH: #(not exist_goal and DEPTH <= MAXDEPTH): #step < 2: 
        print("### DFS with DEPTH {} ###".format(DEPTH))
        depth = 1 # searching depth
        # visited_list = []
        open_list = []
        close_list = []
        
        # begin search after depth 1
        open_list = add_first_node(open_list, current_puzzle_node)
        
        while (len(open_list) > 0): #(not exist_goal and depth < DEPTH): # expand node meaning depth+=1
                        
            # check goal_puzzle is in open_list or not
            # print "check open_list to find goal"
            exist_goal, ind = check_list(open_list, goal_puzzle_node) # ind--the index of goal_puzzle_node in open_list
            if exist_goal:
                goal_puzzle_node = open_list[ind]
                break
				
            current_puzzle_node = open_list[0]
                        
            # delete the node (added in the close_list) in open_list(first node)
            open_list = delete_node(open_list, 0)
                        
            # adding searched node to close_list
            close_list.append(current_puzzle_node)
            
            ##########################################
            #print "close_list"
            #for node in close_list:
            #    node.puzzle.print_puzzle()
            #    print "depth {}".format(node.g_value+1)
            #    print ""
            ##########################################
			
            depth = current_puzzle_node.g_value + 1 # the depth of current node
            #print "searching depth {}".format(depth)
            
            ##########################################
            #print "current_puzzle_node"
            #current_puzzle_node.puzzle.print_puzzle()
            #print "open list"
            #for node in open_list:
            #    node.puzzle.print_puzzle()
            #    print ""
            ##########################################
			
            # reachcing DEPTH, stop expanding
            if depth == DEPTH:                   
                ##########################################
                #print "reaching bottom, visit neighbour" 
                ##########################################
                continue
            
            # expand current_puzzle
            for action in move_action:
                # print "action {}".format(action)
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
                    new_puzzle_node.set_g_value(current_puzzle_node.g_value + 1) # searching cost -- depth-1
                    new_puzzle_node.set_f_value()

                    current_puzzle_node.puzzle.set_current_grid(current_puzzle_node.puzzle.current_grid)  # reset update_grid in current_puzzle

                    #add_first_node(open_list, new_puzzle_node) # debug!!!

                    # check if the expanding node is in close_list and open_list
                    # in DFS, existing in the close list, meaning visited before, but no advantage necessity
                    # need to measure the g_value of node in close list and new node, before continuing decision
                    exist_close, close_ind = check_list(close_list, new_puzzle_node)
                    if exist_close:
                        old_g_value = close_list[close_ind].g_value
                        if new_puzzle_node.g_value < old_g_value:
                            # continuing judging whether the node is in open_list
                            # in DFS, existing in open_list meaning expanded before, and less cost compared with new_puzzle_node expanded currently
                            # because expansion is from deepest branch, instead of least f_value node in open_list
                            exist_open, open_ind = check_list(open_list, new_puzzle_node)
                            if exist_open:
                                continue
                            else:
                                add_first_node(open_list, new_puzzle_node)
                        else:
                            continue
                    else:
                        add_first_node(open_list, new_puzzle_node)
                else:
                    continue # action is not valid, continue to try other actions


        if exist_goal:
            print("### find goal_puzzle in DFS with DEPTH {} ###".format(DEPTH))
            print("### number of searching node in close_list {} ###".format(len(close_list)))
            print("### sum number of visited node {} ###".format(close_list_sum))

            print_action_list(goal_puzzle_node)
            return True, len(close_list)
        #else:
        #    print("### not found in IDS with DEPTH {} ###".format(DEPTH))
        #    print("### number of searching node in close_list {}".format(len(close_list)))

        # restart the DFS
        current_puzzle_node = start_puzzle_node
        # print "start_puzzle_node value {}/{}".format(start_puzzle_node.h_value, start_puzzle_node.g_value)
        DEPTH += 1
        close_list_sum += len(close_list)

        
    if (not exist_goal):
        print("### number of searching node in close_list {}".format(len(close_list)))
        print("No solution in IDS before searching MAXDEPTH {}".format(MAXDEPTH))
        return False, len(close_list_sum)
                                       
