'''
Created on 2021-01-05
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/12
'''

import json
import os
import re

def part_one(input_file):
    '''Solving the first challenge'''
    with open(input_file, encoding='utf-8', mode='r') as file:
        numbers = re.findall(r'-?\d+', file.read())
        return sum([int(i) for i in numbers])

def part_two(input_file):
    '''Solving the second challenge'''
    def sum_non_reds(part):
        if isinstance(part, int):
            return part
        elif isinstance(part, list):
            return sum(sum_non_reds(i) for i in part)
        elif isinstance(part, dict):
            if "red" in part.values():
                return False
            else:
                return sum(sum_non_reds(i) for i in part.values())
        return False

    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        return sum_non_reds(json.load(file))

input_file = f'{os.path.dirname(__file__)}\\input.txt'
print(f'Part 1: {part_one(input_file)}')
print(f'Part 2: {part_two(input_file)}')
