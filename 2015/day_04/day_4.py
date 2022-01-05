'''
Created on 2021-11-28
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/4
'''

from hashlib import md5

def part_one(puzzle):
    '''Solving the first challenge'''
    for number in range(1000000):
        match = md5((puzzle + str(number)).encode()).hexdigest()
        if match[:5] == '00000':
            return number

def part_two(puzzle):
    '''Solving the second challenge'''
    for number in range(10000000):
        match = md5((puzzle + str(number)).encode()).hexdigest()
        if match[:6] == '000000':
            return number

puzzle = "ckczppom" # challenge input is very short this day
print(f'Part 1: {part_one(puzzle)}')
print(f'Part 2: {part_two(puzzle)}')
