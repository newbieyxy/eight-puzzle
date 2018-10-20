# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:03:01 2018

@author: Xuyun Yang

Main function for experiment.
"""

import numpy as np
import pandas as pd
#import copy
from PuzzleWorld import puzzle_world
from AStarMethod import AStar
from GreedyMethod import Greedy
from IDSMethod import IDS
from PuzzleNode import puzzle_node
from util import heuristic_func, generate_random_initial
import time
import argparse

parser = argparse.ArgumentParser('eight-puzzle')
parser.add_argument('--method', type=str, default="IDS", help="IDS, Greedy, AStar_man, AStar_mis")
parser.add_argument('--test-num', type=int, default=1, help="num of test")

args = parser.parse_args()

def main():
    world_shape = 3    
    
    # generate goal grid    
    goal_grid = np.array(range(1,world_shape**2+1)).reshape(world_shape, world_shape)        
    goal_puzzle = puzzle_world(world_shape)
    goal_puzzle.set_current_grid(goal_grid)
    print ("###goal grid###")
    goal_puzzle.print_puzzle()
    goal_puzzle_node = puzzle_node(goal_puzzle)
        
    TEST_NUM = args.test_num
    time_sum = []
    visited_node = []
    success_flag = []

    # initial_grid_record = [] # generate randomly online
    initial_grid_record = np.load('initial_grid.npy')

    title = {'running_time': [], 'visited_time': [], 'success_flag': []}
    df = pd.DataFrame(title)
    
    for _ in range(TEST_NUM):
        print ("test {}".format(_))
        if args.test_num == 1:
            sample_grid = np.array([[3,6,2],[1,4,8],[7,9,5]]) # sample
        else:
            sample_grid = initial_grid_record[_]

        # generate random grid and save
        # current_puzzle_node = generate_random_initial(world_shape, goal_puzzle_node)
        # initial_grid_record.append(current_puzzle_node.puzzle.current_grid)

        # '''
        current_puzzle = puzzle_world(world_shape)
        current_puzzle.set_current_grid(sample_grid)
        current_puzzle_node = puzzle_node(current_puzzle)
        # set node value
        current_puzzle_node.set_h_value(heuristic_func(current_puzzle, goal_puzzle))
        current_puzzle_node.set_g_value(0.)
        current_puzzle_node.set_f_value()
        # '''
        print ("###initial grid###")
        current_puzzle_node.puzzle.print_puzzle()
                        
        if args.method == "IDS":
            start_time = time.time()
            is_solve, close_list_len = IDS(current_puzzle_node, goal_puzzle_node)
            end_time = time.time()
        elif args.method == "Greedy":
            start_time = time.time()
            is_solve, close_list_len = Greedy(current_puzzle_node, goal_puzzle_node)
            end_time = time.time()
        elif args.method == "AStar_man":
            start_time = time.time()
            is_solve, close_list_len = AStar(current_puzzle_node, goal_puzzle_node, "manhattan")
            end_time = time.time()
        elif args.method == "AStar_mis":
            start_time = time.time()
            is_solve, close_list_len = AStar(current_puzzle_node, goal_puzzle_node, "misplacenum")
            end_time = time.time()
        else:
            raise NotImplementedError
           
        time_sum.append(end_time-start_time)
        visited_node.append(close_list_len)
        success_flag.append(is_solve)
    
        print("{}: using time of the solving process: {}s".format(args.method, time_sum[-1]))

        data = pd.Series([end_time-start_time, close_list_len, is_solve], index=['running_time', 'visited_time', 'success_flag'])
        df = df.append(data, ignore_index=True)
        df.to_csv("{}_data.csv".format(args.method))

    print("{} success num {}".format(args.method, np.sum(success_flag)))


    # save initial grid record
    # np.save('initial_grid.npy', initial_grid_record)
    return


if __name__=="__main__":
    main()
