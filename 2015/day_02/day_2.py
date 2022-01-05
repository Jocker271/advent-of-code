'''
Created on 2021-11-28
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/2
'''

import os

def get_challenge_input():
    '''Read input.txt and return content as List'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        lines = file.read().split("\n")
        return lines

def part_one(puzzle):
    '''Solving the first challenge'''
    total_paper = 0
    for line in puzzle:
        length, width, height = [int(i) for i in line.split('x')]
        a = length * width
        b = width * height
        c = height * length
        slack = min(int(s) for s in [a, b, c])        
        present_paper = 2 * a + 2 * b + 2 * c + slack
        total_paper += present_paper
    return total_paper

def part_two(puzzle):
    '''Solving the second challenge'''
    total_ribbon = 0
    for line in puzzle:
        length, width, height = [int(i) for i in line.split('x')]
        sides = [length, width, height]
        sides.remove(max(sides))
        result = 2 * sides[0] + 2 * sides[1] + length * width * height
        total_ribbon += result
    return total_ribbon

puzzle = get_challenge_input()
print(f'Part 1: {part_one(puzzle)}')
print(f'Part 2: {part_two(puzzle)}')
