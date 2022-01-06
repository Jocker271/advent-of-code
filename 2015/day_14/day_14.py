'''
Created on 2021-01-06
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/14
'''

import os

def get_challenge_input():
    '''Read input.txt and return content as List'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        reindeer_data = {}
        for line in file.read().split('\n'):
            parts = line.split(" ")
            name = parts[0]
            speed, time, rest = [int(parts[idx]) for idx in [3, 6, 13]]
            reindeer_data[name] = {'speed': speed, 'time': time, 'rest': rest}
        return reindeer_data

def get_traveled(duration, vals):
    '''Calculates the distance travelled'''
    one_run_time = vals.get('time') + vals.get('rest')
    remaining = duration % one_run_time
    result = duration // one_run_time * vals.get('speed') * vals.get('time')
    if remaining < vals.get('time'):
        result += remaining * vals.get('speed')
    else:
        result += vals.get('speed') * vals.get('time')
    return result

def part_one(puzzle, duration):
    '''Solving the first challenge'''
    results = [get_traveled(duration, vals) for vals in puzzle.values()]
    return max(results)

def part_two(puzzle, duration):
    '''Solving the second challenge'''
    results = dict((reindeer, 0) for reindeer in puzzle)
    distances = results.copy()
    for second in range(1, duration + 1):
        for reindeer, vals in puzzle.items():
            distances[reindeer] = get_traveled(second, vals)
        leads = [k for k, v in distances.items() if v == max(
            distances.values())]
        for winner in leads:
            results[winner] += 1    
    return max(results.values())

puzzle = get_challenge_input()
duration = 2503
print(f'Part 1: {part_one(puzzle, duration)}')
print(f'Part 2: {part_two(puzzle, duration)}')
