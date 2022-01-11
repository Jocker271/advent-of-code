'''
Created on 2021-01-11
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/15
'''

import itertools
import os
import numpy


def get_challenge_input():
    '''Read input.txt and return content as dictionary'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        instructions = {}
        for line in file.read().split('\n'):
            parts = line.replace(",", "").split(' ')
            instructions[parts[0]] = {parts[i]: parts[i + 1] for i in range(
                1, len(parts), 2)}
        return instructions

def compute_max_ingredient_score(puzzle, part_two):
    '''Compute maximum score of ingredient combinations'''
    names = list(puzzle.keys())
    attributes = ['capacity', 'durability', 'flavor', 'texture', 'calories']
    all_scores = set()
    for comb in itertools.combinations_with_replacement(names, 100):
        fact = {attr: 0 for attr in attributes}
        for name in names:
            for attr in attributes:
                fact[attr] += int(puzzle[name][attr]) * comb.count(name)
        if part_two and fact['calories'] != 500:
            continue
        if all(fact[attribute] >= 0 for attribute in attributes[:-1]):
            score = numpy.prod([fact[x] for x in attributes[:-1]])
            all_scores.add(score)
    return max(all_scores)

puzzle = get_challenge_input()
print(f'Part 1: {compute_max_ingredient_score(puzzle, False)}')
print(f'Part 2: {compute_max_ingredient_score(puzzle, True)}')
