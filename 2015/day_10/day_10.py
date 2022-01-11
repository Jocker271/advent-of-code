'''
Created on 2022-01-5
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/10
'''

import re

def look_and_say(sequence, loops):
    regex = re.compile(r'((\d)\2*)')
    sequence = str(sequence)

    def replace(match_obj):
        match = match_obj.group(1)
        return str(len(match)) + match[0]

    for loop in range(loops):
        sequence = regex.sub(replace, sequence)
    return sequence

puzzle = 1113222113 # challenge input is very short this day
part_one = look_and_say(puzzle, 40)
print(f'Part 1: {len(part_one)}')
part_two = look_and_say(part_one, 10)
print(f'Part 2: {len(part_two)}')


################################ code relicts ################################

def look_and_say_first_try(sequence, loops):
    '''My first attempt to solve the puzzle, but too slow for 50 loop passes.
    So I had to find a better way -> look_and_say()
    '''
    sequence = str(sequence)

    def count_char_in_row(sub_sequence):
        char = sub_sequence[0]
        count = 1
        if len(sub_sequence) > 2 and char == sub_sequence[1]:
            count += count_char_in_row(sub_sequence[1:])
        return count

    for loop in range(loops):
        new_sequence = []
        skip = 0
        for idx, char in enumerate(sequence):
            if skip > 0:
                skip -= 1
            else:
                count = count_char_in_row(sequence[idx:])
                new_sequence.extend([str(count), char])
                skip = count - 1
        sequence = "".join(new_sequence)
    return sequence
