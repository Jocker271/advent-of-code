'''
Created on 2021-01-11
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/16
'''

import os

def get_challenge_input():
    '''Read input.txt and return content as List'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        lines = file.read().replace(":", "").replace(",", "").split('\n')
        sues = [{line.split(" ")[i]: int(line.split(" ")[i+1]) for i in range(
            0, len(line.split(" ")), 2)} for line in lines]
        return sues

def part_one(puzzle, mfcsam):
    '''Solving the first challenge'''
    for line in puzzle:
        compounds = [k for k in line.keys() if k != "Sue"]
        if all(line[comp] == mfcsam[comp] for comp in compounds):
            return line["Sue"]
    return False

def part_two(puzzle, mfcsam):
    '''Solving the second challenge'''
    for line in puzzle:
        compounds = [k for k in line.keys() if k != "Sue"]
        checks = []
        for comp in compounds:
            if comp in ['cats', 'trees']:
                checks.append(line[comp] > mfcsam[comp])
            elif comp in ['pomeranians', 'goldfish']:
                checks.append(line[comp] < mfcsam[comp])
            else:
                checks.append(line[comp] == mfcsam[comp])
        if all(checks):
            return line["Sue"]
    return False

def main():
    mfcsam = {'children': 3, 'cats': 7, 'samoyeds': 2,
        'pomeranians': 3, 'akitas': 0, 'vizslas': 0,
        'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
    puzzle = get_challenge_input()
    print(f'Part 1: {part_one(puzzle, mfcsam)}')
    print(f'Part 2: {part_two(puzzle, mfcsam)}')

if __name__ == "__main__":
    main()
