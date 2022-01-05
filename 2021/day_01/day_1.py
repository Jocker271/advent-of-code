'''
Created on 2021-12-01
by Johannes Wehden - Jocker271
------------------------------
Find this task at https://adventofcode.com/2021/day/1
'''

import os

def get_challenge_input():
    '''Read input.txt and return content as List'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        lines = file.read().split('\n')
        lines = list(map(int, lines)) #convert Strings to Integers
        return lines

def part_one(puzzle):
    '''Solving the first challenge'''
    result = 0
    line_before = puzzle[0]
    for line in puzzle:
        if line > line_before:
            result += 1
        line_before = line
    return result

def part_two(puzzle):
    '''Solving the second challenge'''
    result = 0
    sum_before  = sum(puzzle[:3])
    for i in range(len(puzzle[:-2])):
        line_sum = sum(puzzle[i:i+3])
        if line_sum > sum_before:
            result += 1
        sum_before = line_sum
    return result

puzzle = get_challenge_input()
print(f'Part 1: {part_one(puzzle)}')
print(f'Part 2: {part_two(puzzle)}')
