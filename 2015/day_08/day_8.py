'''
Created on 2022-01-05
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/8
'''

import os

def get_challenge_input():
    '''Read input.txt and return content as List'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        lines = file.read().split('\n')
        return lines

def part_one(puzzle):
    '''Solving the first challenge'''
    return sum([len(line) - len(eval(line)) for line in puzzle])

def part_two(puzzle):
    '''Solving the second challenge'''
    return sum([line.count('\\') + line.count('"') + 2 for line in puzzle])

puzzle = get_challenge_input()
print(f'Part 1: {part_one(puzzle)}')
print(f'Part 2: {part_two(puzzle)}')
