'''
Created on 2022-01-11
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/17
'''

from itertools import combinations
import os

def get_challenge_input():
    '''Read input.txt and return content as List'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        return [int(line) for line in file.read().split('\n')]

def get_combinations(components):
    results = []
    for length in range(len(components) + 1):
        for comb in combinations(components, length):
            if sum(comb) == 150:
                results.append(comb)
    return results

def part_one(puzzle):
    '''Solving the first challenge'''
    return len(get_combinations(puzzle))

def part_two(puzzle):
    '''Solving the second challenge'''
    sizes = [len(ls) for ls in get_combinations(puzzle)]
    return sizes.count(min(sizes))

puzzle = get_challenge_input()
print(f'Part 1: {part_one(puzzle)}')
print(f'Part 2: {part_two(puzzle)}')
