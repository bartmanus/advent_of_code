#!/usr/bin/env python3

"""
Follow relative instructions on keypads to figure out the access code.
Starting position is key 5. Each input line ends on digit which is
appended to the code.
Disregard instructions which direct movement out of the keypad.
Keyboard layout may contain None which is a dummy element used for alignment.
"""

KEYPADS = {'part1': {'layout': [['1','2','3'], ['4','5','6'], ['7','8','9']], \
                     'origin': {'row': 1, 'column': 1}}, \
           'part2': {'layout': [[None, None, '1'], \
                                [None,  '2', '3', '4'], \
                                [  '5', '6', '7', '8', '9'], \
                                [None,  'A', 'B', 'C'], \
                                [None, None, 'D']], \
                     'origin': {'row': 2, 'column': 0}}}

def valid_input(instructions):
    """
    Validate input to be a multi-line string containing directions [UDLR]+
    :param instructions: Multiline string input
    :return: Boolean value whether input is valid
    """
    from re import match
    m = match(r'[UDLR]+', ''.join(instructions))
    return m is not None and m.span() == (0, sum(len(i) for i in instructions))

def exists_position(layout, row, column):
    """
    Checks whether given row and column indices represent a valid position in
    the layout.
    Check whether row is inside the range od rows, check whether the column is
    at or below the right edge of the keypad and finally check the left edge is
    not a placeholder.
    :param layout: 2D list representing keypad layout
    :param row: row index integer
    :param column: column index integer
    :return: boolean whether the position is a valid key
    """
    return row in range(len(layout)) and \
            column in range(len(layout[row])) and \
            layout[row][column] is not None

def keypad_move(layout, position, moves):
    """
    Follows a sequence of moves on a keypad from a starting position. Ignores
    moves over the keyboard boundary.
    :param position: Dictionary with row and column keys and integer values
    :param moves: A series of moves to make on the keyboard
    :return: The end position.
    """
    for move in moves:
        if move == 'U' and exists_position(layout, position['row']-1, position['column']):
            position['row'] -= 1
        elif move == 'D' and exists_position(layout, position['row']+1, position['column']):
            position['row'] += 1
        elif move == 'R' and exists_position(layout, position['row'], position['column']+1):
            position['column'] += 1
        elif move == 'L' and exists_position(layout, position['row'], position['column']-1):
            position['column'] -= 1
    return position

def keypad(instructions, pad='part1'):
    """
    Method receives complete instructions and builds the complete access code.
    :param instructions: Multiline string with instructions
    :param pad: String selecting a layout from the KEYPADS
    :return code: String holding access code
    """
    assert pad in KEYPADS
    keypad = KEYPADS.get(pad)
    position = keypad['origin']
    code = []
    for instruction in instructions:
        position = keypad_move(keypad['layout'], position.copy(), instruction)
        code.append(keypad['layout'][position['row']][position['column']])
    return ''.join((symbol for symbol in code))

if __name__ == '__main__':
    """
    When module is executed directly, perform some tests.
    """
    TEST_CASES = [ \
        {'keypad': 'part1', \
         'input': ['ULL','RRDDD','LURDL','UUUUD'], \
         'output': '1985'}, \
        {'keypad': 'part2', \
         'input': ['ULL','RRDDD','LURDL','UUUUD'], \
         'output': '5DB3'}, \
        {'keypad': 'part2', \
         'input': ['RU','RU','DR','DR','LD','LD','UL','UL','RR'], \
         'output': '2149CDA57'} \
    ]
    for case in TEST_CASES:
        current = keypad(case['input'], pad=case['keypad'])
        result = 'PASS' if current == case['output'] else 'FAIL'
        print('Expecting {}, computed {}. Test {}!'.format(\
                case['output'], current, result))

