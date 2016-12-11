#!/usr/bin/env python3

"""
Part 1: Taxicab (non-Euclidean) distance from origin following relative
directions on a plane.
Starting direction is North.
Part 2: Taxicab distance to the first crossing of the walked path.

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
 - State: X -> 1, Y -> 0, - -> -1, + -> 1
 - Input: R -> +1, L -> -1
For part 2 of the puzzle, all visited vertices are generated and searched.
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
    """
    Returns two taxicab distances from origin point:
    1. Distance to point where instructions lead.
    2. Distance to point where the first path intersection occurs.
    """
    DIRECTION_MAPPING = {'R':1, 'L':-1}
    state = {'axis': 0, 'sign': +1}
    path = [[0, 0]]
    for instruction in instructions.split(', '):
        direction = DIRECTION_MAPPING[instruction[0]]
        steps = int(instruction[1:])
        state = new_state(state, direction)
        axis_dir = state['sign']
        pos_x, pos_y = path[-1]
        if state['axis'] == 0:
            # movement axis is 0/Y
            path.extend(([pos_x, y] for y in range(pos_y + axis_dir * 1, \
                               pos_y + axis_dir * (1 + steps), axis_dir)))
        else:
            # movement axis is 1/X
            path.extend(([x, pos_y] for x in range(pos_x + axis_dir * 1, \
                               pos_x + axis_dir * (1 + steps), axis_dir)))
    distance_total, distance_crossing = sum((abs(s) for s in path[-1])), None
    for step_num in range(1, len(path)):
        if path[step_num] in path[:step_num]:
            distance_crossing = sum((abs(s) for s in path[step_num]))
            break
    return distance_total, distance_crossing
        
if __name__ == '__main__':
    """
    When module is executed directly, perform some tests.
    """
    TEST_CASES = [ \
        {'input': 'R2, L3', 'output': (5, None,)}, \
        {'input': 'R2, R2, R2', 'output': (2, None,)}, \
        {'input': 'R5, L5, R5, R3', 'output': (12, None,)}, \
        {'input': 'R8, R4, R4, R8', 'output': (8, 4,)} \
    ]
    try:
        for case in TEST_CASES:
            assert taxicab(case['input']) == case['output']
        print('Tests successfully passed!')
    except AssertionError:
        print('Test FAILURE!')

