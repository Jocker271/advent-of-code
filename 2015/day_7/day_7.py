'''
Created on 2021-11-30
by Johannes Wehden - (Jocker271)
--------------------------------
Find this challenge at https://adventofcode.com/2015/day/7
'''

import os

class Wire(object):

    def __init__(self, line):
        self._line = line
        self.parse_line(line)

    def parse_line(self, line):
        parts = line.split()
        self.output = parts[-1]
        left = parts[:-2]
        self.op = 'ASSIGN'
        for op in ['NOT', 'AND', 'OR', 'LSHIFT', 'RSHIFT']:
            if op in left:
                self.op = op
                left.remove(op)
        self.inputs = [int(i) if i.isdigit() else i for i in left]

    def reset(self):
        self.parse_line(self._line)

    def evaluate(self):
        if self.op == 'ASSIGN':
            return int(self.inputs[0])
        elif self.op == 'NOT':
            return int(65535 - self.inputs[0])
        elif self.op == 'AND':
            return int(self.inputs[0] & self.inputs[1])
        elif self.op == 'OR':
            return int(self.inputs[0] | self.inputs[1])
        elif self.op == 'LSHIFT':
            return int(self.inputs[0] << self.inputs[1])
        elif self.op == 'RSHIFT':
            return int(self.inputs[0] >> self.inputs[1])
        else:
            raise ValueError('invalid operator')

    def fill_inputs(self, signals):
        self.inputs = [signals[i] if i in signals else i for i in self.inputs]

    def iscomplete(self):
        return all([isinstance(i, int) for i in self.inputs])


def get_challenge_input():
    '''Read input.txt and return content as List'''
    input_file = f'{os.path.dirname(__file__)}\\input.txt'
    with open(input_file, encoding='utf-8', mode='r') as file:
        lines = file.read().split('\n')
        return lines

def evaluate_circuit(wires, signals):
    '''assign wire connections'''
    local_wires = list(wires)
    while len(local_wires) > 0:
        new_wires = []
        for wire in wires:
            if wire.iscomplete():
                signals[wire.output] = wire.evaluate()
            else:
                wire.fill_inputs(signals)
                new_wires.append(wire)
        local_wires = new_wires
    return signals

def part_one(wires):
    '''Solving the first challenge'''
    return evaluate_circuit(wires, {})['a']

def part_two(wires):
    '''Solving the second challenge'''
    signals = evaluate_circuit(wires, {})
    for wire in wires:
        wire.reset()
    wires = [wire for wire in wires if wire.output != 'b']
    return evaluate_circuit(wires, {'b': signals['a']})["a"]

wires = [Wire(line) for line in get_challenge_input()]
print(f'Part 1: {part_one(wires)}')
print(f'Part 2: {part_two(wires)}')
