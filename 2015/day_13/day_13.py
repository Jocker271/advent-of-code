'''
Created on 2021-01-05
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/13
'''

import os

def get_challenge_input():
    '''Read input.txt and return content as List'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        return file.read().split('\n')

def compute(puzzle, names):
    happiness = {}
    for person in names:
        for neighbor in names:
            if neighbor != person:
                happiness[frozenset((person, neighbor))] = 0
    for line in puzzle:
        parts = line[:-1].split(" ")
        person  = parts[0]
        measure = int(f'-{parts[3]}' if parts[2] == "lose" else parts[3])
        neighbor = parts[-1]
        happiness[frozenset((person, neighbor))] += measure

    def get_best(remainder, this, end):
        if len(remainder) == 0:
            return happiness[frozenset((this, end))]
        result = 0
        for next in remainder:
            attempt = get_best(remainder.difference({next}), next, end)
            result = max(result, happiness[frozenset((this, next))] + attempt)
        return result

    start = names.pop()
    return get_best(names, start, start)

def part_one(puzzle):
    names = set(l.split(' ')[0] for l in puzzle)
    return compute(puzzle, names)

def part_two(puzzle):
    names = set(l.split(' ')[0] for l in puzzle)
    names.add('me')
    return compute(puzzle, names)

puzzle = get_challenge_input()
print(f'Part 1: {part_one(puzzle)}')
print(f'Part 2: {part_two(puzzle)}')
