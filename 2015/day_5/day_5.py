'''
Created on 2021-11-29
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/5
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
    result = 0
    for line in puzzle:
        if not any(x in line for x in ["ab", "cd", "pq", "xy"]):
            if sum([line.count(vowel) for vowel in "aeiou"]) >= 3:
                for idx, char in enumerate(line):
                    if idx > 0 and char == line[idx - 1]:
                        result += 1
                        break
    return result

def part_two(puzzle):
    '''Solving the second challenge'''
    result = 0
    for line in puzzle:
        rule_one = False
        rule_two = False
        for i in range(len(line) - 3):
            sub = line[i: i + 2]
            if sub in line[i + 2:]:
                rule_one = True
                break
        for idx, char in enumerate(line):
            if idx > 1 and char == line[idx - 2]:
                rule_two = True
                break
        if rule_one and rule_two:
            result += 1
    return result

puzzle = get_challenge_input()
print(f'Part 1: {part_one(puzzle)}')
print(f'Part 2: {part_two(puzzle)}')
