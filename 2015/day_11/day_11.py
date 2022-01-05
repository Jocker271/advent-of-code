'''
Created on 2021-01-05
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/11
'''

import string

def check_password(pw):
    '''Check that all requirements are met.'''
    alphabet = list(string.ascii_lowercase)
    alpha_row = False
    for idx, char in enumerate(pw[:-2]):
        char_index = alphabet.index(char)
        alpha_char = lambda n: pw[idx + n] == alphabet[char_index + n]
        if char_index < 24 and alpha_char(1) and alpha_char(2):
            alpha_row = True
            break
    if not alpha_row:
        return False
    if any(letter in pw for letter in "iol"):
        return False
    pairs = set()
    for idx, char in enumerate(pw[:-1]):
        if char == pw[idx + 1]:
            pairs.add(char)
    if not len(pairs) >= 2:
        return False
    return True

def get_next_string(pw):
    '''Increasing password string by one.'''
    password = ""
    if( (ord(pw[len(pw)-1]) - 96) == 26 ):
        password += get_next_string(pw[:len(pw) - 1]) + "a"
    else:
        return (pw[:len(pw) - 1] + chr(ord(pw[len(pw) - 1]) + 1))
    return password

def next_password(password):
    '''Searching for the next available password.'''
    pw_check = False
    while not pw_check:
        password = get_next_string(password)
        pw_check = check_password(password)
    return password

puzzle = "hxbxwxba"
first_password = next_password(puzzle)
print(f'Part 1: {first_password}')
print(f'Part 2: {next_password(first_password)}')
