'''
Created on 2022-01-16
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/18
'''

import os
import numpy as np

def get_challenge_input():
    '''Read input.txt and return content as parsed Matrix'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        grid = np.zeros((100,100), dtype=bool)
        for idx, line in enumerate(file.read().split('\n')):
            for idy, char in enumerate(line):
                grid[idx, idy] = True if char == "#" else False
        return grid

def compute_new_grid(grid):
    ''' update all lights in grid simultaneously
        (could be faster, but at least it works) '''
    result_grid = grid.copy()
    for idy in range(100):
        for idx in range(100):
            neighbors = []
            neighbor_indexes = [(a, b) for a in range(
                idx-1, idx+2) for b in range(idy-1, idy+2)]
            for index in neighbor_indexes:
                if not index == (idx, idy):
                    if any(a < 0 or a > 99 for a in index):
                        neighbors.append(False)
                    else:
                        neighbors.append(grid[index])
            if grid[idx, idy] and sum(neighbors) not in [2, 3]:
                result_grid[idx, idy] = False
            elif not grid[idx, idy] and sum(neighbors) == 3:
                result_grid[idx, idy] = True
    return result_grid

def part_one(grid):
    '''Solving the first challenge'''
    for i in range(100):
        grid = compute_new_grid(grid)
    return np.sum(grid)

def part_two(grid):
    '''Solving the second challenge'''
    for i in range(101):
        for index in [(0, 0), (0, 99), (99, 0), (99, 99)]:
            grid[index] = True
        if i < 100:
            grid = compute_new_grid(grid)
    return np.sum(grid)

puzzle = get_challenge_input()
print(f'Part 1: {part_one(puzzle)}')
print(f'Part 2: {part_two(puzzle)}')
