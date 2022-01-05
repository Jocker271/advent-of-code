'''
Created on 2021-12-02
by Johannes Wehden - Jocker271
------------------------------
Find this task at https://adventofcode.com/2021/day/2
'''

import os

def get_challenge_input():
    '''Read input.txt and return content as List'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        lines = file.read().split('\n')
        # lines = list(map(int, lines)) #convert Strings to Integers
        return lines

def part_one(puzzle):
    '''Solving the first challenge'''
    direction =  {'forward': 0, 'down': 0, 'up': 0}
    for line in puzzle:
        key, value = line.split(" ")
        direction[key] = direction.get(key) + int(value)
    vertical = direction.get('down') - direction.get('up')
    result = vertical * direction.get('forward')
    return result

def part_two(puzzle):
    '''Solving the second challenge'''
    direction =  {'horizontal': 0, 'depth': 0, 'aim': 0}
    for line in puzzle:
        key, value = line.split(" ")
        if key == 'down':
            direction['aim'] = direction.get('aim') + int(value)
        elif key == 'up':
            direction['aim'] = direction.get('aim') - int(value)
        elif key == "forward":
            direction['horizontal'] = direction.get('horizontal') + int(value)
            aim_value = direction.get('aim') * int(value)
            direction['depth'] = direction.get('depth') + aim_value
    result = direction.get('horizontal') * direction.get('depth')
    return result

puzzle = get_challenge_input()
print(f'Part 1: {part_one(puzzle)}')
print(f'Part 2: {part_two(puzzle)}')
