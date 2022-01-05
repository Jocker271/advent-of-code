'''
Created on 2021-01-5
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/9
'''

import os
from collections import defaultdict
from itertools import permutations

def get_challenge_input():
    '''Read input.txt and return content as List'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        lines = file.read().split('\n')
        return lines

def get_distances(puzzle):
    '''compute all distances'''
    places = set()
    graph = defaultdict(dict)
    for line in puzzle:
        src, _, dst, _, dist = line.split()
        places.update([src, dst])
        graph[src][dst] = int(dist)
        graph[dst][src] = int(dist)
    distances = []
    for perm in permutations(places):
        distances.append(sum(map(
            lambda x, y: graph[x][y], perm[:-1], perm[1:])))
    return distances

puzzle = get_challenge_input()
distances = get_distances(puzzle)
print(f'Part 1: {min(distances)}')
print(f'Part 2: {max(distances)}')
