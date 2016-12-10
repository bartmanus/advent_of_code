#!/usr/bin/env python3

"""
Taxicab (non-Euclidean) distance from origin following relative directions
on a plane.
Starting direction is North.

Example:
 - Input:  R5, L5, R5, R3
 - Output: 12

Solution: Mealy finite state machine determines movement heading.
Heading is a compound of axis and direction on the axis.
 - States = {X+, X-, Y+, Y-}
 - Inputs = {Rn, Ln}
 - Transition function: s is any sign, ~ is negation
    - (Xs, Rn)->(Y~s)
    - (Xs, Ln)->(Ys)
    - (Ys, Rn)->(Xs)
    - (Ys, Ln)->(X~s)
Implementation:
 - State: X -> 0, Y -> 1, - -> -1, + -> 1
 - Input: R -> +1, L -> -1
"""
import sys

def new_state(current_state, direction):
    """
    Calculates new heading from current heading and relative direction.
    """
    new_axis = (current_state['axis']+1) & 1
    multiplier = -1 if current_state['axis'] == 0 and direction == 1 or \
                       current_state['axis'] == 1 and direction == -1 else 1 
    new_sign = current_state['sign'] * multiplier
    return {'axis': new_axis, 'sign': new_sign}

def taxicab(instructions):
    DIRECTION_MAPPING = {'R':1, 'L':-1}
    origin_vector = [0, 0]
    state = {'axis': 0, 'sign': +1}
    for instruction in instructions.split(', '):
        direction = DIRECTION_MAPPING[instruction[0]]
        steps = int(instruction[1:])
        state = new_state(state, direction)
        origin_vector[state['axis']] += steps * state['sign']
    distance = sum((abs(s) for s in origin_vector))
    return distance
        
if __name__ == '__main__':
    instructions = sys.argv[1] if len(sys.argv) == 2 \
                               else input('Instructions, please: ')
    print('Taxicab distance is {}.'.format(taxicab(instructions)))

