'''
Created on 2021-11-28
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/1
'''

import os

def get_challenge_input():
    '''Read input.txt and return content as List'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        lines = file.read()
        return lines

def part_one(puzzle):
    '''Solving the first challenge'''
    return puzzle.count("(") - puzzle.count(")")

def part_two(puzzle):
    '''Solving the second challenge'''
    floor = 0
    steps = {"(": 1, ")": -1}
    for idx, char in enumerate(puzzle):
        floor += steps[char]
        if floor == -1:
            return idx + 1
    return False

puzzle = get_challenge_input()
print(f'Part 1: {part_one(puzzle)}')
print(f'Part 2: {part_two(puzzle)}')
