'''
Created on 2021-12-01
by Johannes Wehden - (Jocker271)
--------------------------------
This script creates all folders and template files for the entered year,
if they do not already exist. The Python template is at the end of this file.
'''

import os
from datetime import datetime

def main():
    '''Retrieves user input and executes this script.'''
    while True:
        print('For which year do you want to create the file structure?')
        year = input("Year: ") or str(datetime.now().year)
        if year.isdigit() and len(year) == 4:
            create_file_structure(year)
            break
        print(f'{year} is not a possible value.')
    print('✓ File structure successfully created')

def create_file_structure(year):
    '''Creates python and text files for each day in a seperate folder.'''
    parent = os.getcwd()
    folder_path = os.path.join(parent, year)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    template = get_template().replace('{year}', year)
    for day in range(1, 26):
        day_folder = os.path.join(folder_path, f'day_{str(day).zfill(2)}')
        if not os.path.exists(day_folder):
            os.mkdir(day_folder)
            py_file_path = os.path.join(day_folder, f'day_{str(day)}.py')
            txt_file_path = os.path.join(day_folder, 'input.txt')
            with open(py_file_path, encoding='utf-8', mode='w+') as py_file:
                py_file.write(template.replace('{day}', str(day)))
                #py_file.close()
            open(txt_file_path, encoding='utf-8', mode='x').close()

def get_template():
    '''Returns template inside this file (look at the end) as String.'''
    template = ''
    with open(__file__, encoding='utf-8', mode='r') as this_file:
        start_template = False
        for line in this_file:
            if start_template:
                template += line[2:] if len(line) > 2 else '\n'
            elif line == '# --- TEMPLATE STARTS HERE ---\n':
                start_template = True
    return template

main()

# --- TEMPLATE STARTS HERE ---
# '''
# Created on {year}-12-{day}
# by Johannes Wehden - (Jocker271)
# --------------------------------
# Find this challenge at https://adventofcode.com/{year}/day/{day}
# '''

# import os

# def get_challenge_input():
#     '''Read input.txt and return content as List'''
#     input_file = f'{os.path.dirname(__file__)}\\input.txt'
#     with open(input_file, encoding='utf-8', mode='r') as file:
#         lines = file.read().split('\n')
#         # lines = [int(line) for line in lines]
#         return lines

# def part_one(puzzle):
#     '''Solving the first challenge'''
#     result = 0
#     for line in puzzle:
#         if line:
#             result += 1
#     return str(result)

# def part_two(puzzle):
#     '''Solving the second challenge'''
#     result = 0
#     for idx, line in enumerate(puzzle):
#         if line:
#             result = idx
#             break
#     return str(result)

# puzzle = get_challenge_input()
# print(f'Part 1: {part_one(puzzle)}')
# print(f'Part 2: {part_two(puzzle)}')
