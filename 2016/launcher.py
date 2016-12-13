#!/usr/bin/env python3

"""
Launcher for AoC 2016 puzzles.
Handles puzzle selection and puzzle input.
"""

import day_1_no_time_for_a_taxicab as d1
import day_2_bathroom_security as d2

def run_taxicab():
    while True:
        instructions = input('Instructions in <dir><steps>[, <dir><steps>]* format, please: ')
        try:
            assert instructions != None and len(instructions) > 1
            for instruction in instructions.split(', '):
                assert instruction[0] in ['R', 'L']
                int(instruction[1:])
            break
        except AssertionError:
            print('Invalid direction detected, please check your input!')
        except ValueError:
            print('Invalid step format detected, please check your input!')
    distance_total, distance_crossing = d1.taxicab(instructions)
    print('Taxicab distance to final destination is {}.'.format(distance_total))
    print('Taxicab distance to first path crossing is {}.'.format(distance_crossing))

def run_keypad():
    instructions = []
    while len(instructions) == 0:
        print('''Please input 3x3 keypad movement instructions. End input with by feeding
an empty line. For each code digit input one line in [UDLR]+ format. Movement
starts in the middle at digit 5.''')
        while True:
            instructions.append(input())
            if instructions[-1] == '':
                instructions.pop()
                if len(instructions) > 0:
                    break
        if d2.valid_input(instructions):
            break
        else:
            print('Invalid instructions, please retry!')
            print(str(instructions))
            instructions.clear()
    for keypad in d2.KEYPADS:
        code = d2.keypad(instructions, pad=keypad) 
        print('Keypad code to {} is {}.'.format(keypad, code))

if __name__ == '__main__':
    AVAILABLE_PUZZLES = {1: run_taxicab, 2:run_keypad}
    print('Welcome to inifinity! Try an available solution to AoC 2016 puzzles in', \
            list(AVAILABLE_PUZZLES.keys()), 'or enter EOF to quit!')
    while True:
        puzzle = None
        try:
            puzzle = int(input('Please select a puzzle: '))
            if puzzle not in AVAILABLE_PUZZLES:
                print('That puzzle\'s solution is not available! Try one of', \
                        list(AVAILABLE_PUZZLES.keys()))
                puzzle = None
            else:
                AVAILABLE_PUZZLES[puzzle]()
        except ValueError:
            print('Please input an integer!')
        except EOFError:
            print('\nThanks for playing, happy holidays!')
            break 
