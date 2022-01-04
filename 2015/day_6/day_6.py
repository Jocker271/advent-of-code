'''
Created on 2021-11-29
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/6
'''

import os
import re
import numpy as np

def get_challenge_input():
    '''Read input.txt and return content as List'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        lines = file.read().split('\n')
        return lines

def part_one(puzzle):
    '''Solving the first challenge'''
    array = np.zeros((1000,1000), dtype=bool)
    regex = r'(\w+) (\d+),(\d+) through (\d+),(\d+)'
    for line in puzzle:
        command, x0, y0, x1, y1 = re.search(regex, line).groups()
        corners = [[x0, x1], [y0, y1]]
        x_slice, y_slice = [slice(int(a), int(b) + 1) for a, b in corners]
        if command == 'toggle':
            array[x_slice, y_slice] = np.invert(array[x_slice, y_slice])
        else:
            array[x_slice, y_slice] = ['off', 'on'].index(command)
    return sum(sum(array))

def part_two(puzzle):
    '''Solving the second challenge'''
    array = np.zeros((1000,1000), dtype=int)
    regex = r'(\w+) (\d+),(\d+) through (\d+),(\d+)'
    for line in puzzle:
        command, x0, y0, x1, y1 = re.search(regex, line).groups()
        corners = [[x0, x1], [y0, y1]]
        x_slice, y_slice = [slice(int(a), int(b) + 1) for a, b in corners]
        transform = {'on': 1, 'off': -1, 'toggle': 2}
        array[x_slice, y_slice] += transform.get(command)
        array[array < 0] = 0 # cannot be less than 0 bright
    return sum(sum(array))

puzzle = get_challenge_input()
print(f'Part 1: {part_one(puzzle)}')
print(f'Part 2: {part_two(puzzle)}')
