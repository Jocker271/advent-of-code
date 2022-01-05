'''
Created on 2021-12-3
by Johannes Wehden - (Jocker271)
--------------------------------
Find this task at https://adventofcode.com/2021/day/3
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
    '''Solving the first Task'''
    gamma = ""
    for index in range(len(puzzle[0])):
        bits = [line[index] for line in puzzle]
        gamma += max(bits, key = bits.count)
    epsilon = "".join(['0'  if char == '1' else '1' for char in gamma])
    result = int(gamma, 2) * int(epsilon, 2)
    return str(result)

def part_two(puzzle):
    '''Solving the second Task'''
    def get_attribute_value(prever, reject):
        attr_list = puzzle
        index = 0
        while len(attr_list) > 1:
            bits = [line[index] for line in attr_list]
            match = prever if bits.count('1') >= bits.count('0') else reject
            attr_list = [num for num in attr_list if num[index] == match]
            index += 1
        return int(attr_list[0], 2)
    oxygen = get_attribute_value('1', '0')
    co2 = get_attribute_value('0', '1')
    return str(oxygen * co2)

puzzle = get_challenge_input()
print(f'Part 1: {part_one(puzzle)}')
print(f'Part 2: {part_two(puzzle)}')
