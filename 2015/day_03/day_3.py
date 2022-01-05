'''
Created on 2021-11-28
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/3
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
    last_house = (0, 0)
    house_set = {last_house}
    horizontal = {"<": -1, ">": 1}
    vertival = {"v": -1, "^": 1}
    for direction in puzzle:
        x, y = last_house
        if direction in ["<", ">"]:
            x += horizontal[direction]
        else:
            y += vertival[direction]
        last_house = (x, y)
        house_set.add((x, y))
    return len(house_set)

def part_two(puzzle):
    '''Solving the second challenge'''
    last_houses = [(0, 0),(0,0)]
    house_set = {(0, 0)}
    horizontal = {"<": -1, ">": 1}
    vertival = {"v": -1, "^": 1}
    for idx, direction in enumerate(puzzle):
        x, y = last_houses[(idx % 2)]
        if direction in ["<", ">"]:
            x += horizontal[direction]
        else:
            y += vertival[direction]
        last_houses[(idx % 2)] = (x, y)
        house_set.add((x, y))
    return len(house_set)

puzzle = get_challenge_input()
print(f'Part 1: {part_one(puzzle)}')
print(f'Part 2: {part_two(puzzle)}')
