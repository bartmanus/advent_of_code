#!/usr/bin/env python3

"""
Follow relative instructions on a 3x3 keypad to figure out the code.
Starting position is center, 5. Each input line ends on digit which is
appended to the code.
Disregard instructions which direct movement out of the keypad.
"""

KEYPAD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def valid_input(instructions):
    """
    Validate input to be a multi-line string containing directions [UDLR]+
    :param instructions: Multiline string input
    :return: Boolean value whether input is valid
    """
    from re import match
    m = match(r'[UDLR]+', ''.join(instructions))
    return m is not None and m.span() == (0, sum(len(i) for i in instructions))

def keypad_move(position, moves):
    """
    Follows a sequence of moves on a keypad from a starting position. Ignores
    moves over the keyboard boundary.
    :param position: Dictionary with row and column keys and integer values
    :param moves: A series of moves to make on the keyboard
    :return: The end position.
    """
    for move in moves:
        if move == 'U':
            position['row'] -= 1 if position['row'] > 0 else 0
        elif move == 'D':
            position['row'] += 1 if position['row'] < 2 else 0
        elif move == 'R':
            position['column'] += 1 if position['column'] < 2 else 0
        elif move == 'L':
            position['column'] -= 1 if position['column'] > 0 else 0
    return position

def keypad(instructions):
    """
    Method receives complete instructions and builds the complete access code.
    :param instructions: Multiline string with instructions
    :return code: String holding access code
    """
    position = {'row': 1, 'column': 1}
    code = []
    for instruction in instructions:
        position = keypad_move(position.copy(), instruction)
        code.append(KEYPAD[position['row']][position['column']])
    return ''.join((str(cipher) for cipher in code))

if __name__ == '__main__':
    """
    When module is executed directly, perform some tests.
    """
    TEST_CASES = [ \
        {'input': ['ULL','RRDDD','LURDL','UUUUD'], 'output': '1985'} \
    ]
    try:
        for case in TEST_CASES:
            assert keypad(case['input']) == case['output']
        print('Tests successfully passed!')
    except AssertionError:
        print('Test FAILURE!')

