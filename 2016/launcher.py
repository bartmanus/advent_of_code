#!/usr/bin/env python3

"""
Launcher for AoC 2016 puzzles.
Handles puzzle selection and puzzle input.
"""

import day_1_no_time_for_a_taxicab as d1

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

if __name__ == '__main__':
    AVAILABLE_PUZZLES = {1: run_taxicab}
    print('Welcome to inifinity! Try an available solution to AoC 2016 puzzles in', \
            list(AVAILABLE_PUZZLES), 'or enter EOF to quit!')
    while True:
        puzzle = None
        try:
            puzzle = int(input('Please select a puzzle: '))
            if puzzle is None:
                continue
            if puzzle not in AVAILABLE_PUZZLES:
                print('That puzzle\'s solution is not available! Try one of', list(AVAILABLE_PUZZLES))
                puzzle = None
            else:
                AVAILABLE_PUZZLES[puzzle]()
        except ValueError:
            print('Please input an integer!')
        except EOFError:
            print('\nThanks for playing, happy holidays!')
            break 
