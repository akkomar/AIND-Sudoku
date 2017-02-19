from collections import defaultdict

from utils import *

assignments = []


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    for unit in unitlist:
        # Find all instances of naked twins
        two_value_boxes = [u for u in unit if len(values[u]) == 2]
        values_to_boxes = defaultdict(set)
        for box in two_value_boxes:
            values_to_boxes[values[box]].add(box)
        naked_twins = {value: boxes for value, boxes in values_to_boxes.items() if len(boxes) == 2}

        # Eliminate the naked twins as possibilities for their peers
        for twin_values, twin_boxes in naked_twins.items():
            for peer in (box for box in unit if box not in twin_boxes):
                for v in twin_values:
                    values = assign_value(values, peer, values[peer].replace(v, ''))

    return values


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = ['123456789' if c == '.' else c for c in grid]
    return dict(zip(boxes, values))


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return


def eliminate(values):
    for box, v in values.items():
        if len(v) == 1:
            for peer in peers[box]:
                # remove this value from set of values of all its peers
                new_value = values[peer].replace(v, '')
                values = assign_value(values, peer, new_value)
    return values


def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            digit_boxes = [box for box in unit if digit in values[box]]
            if len(digit_boxes) == 1:
                values = assign_value(values, digit_boxes[0], digit)
    return values


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Eliminate Strategy
        values = eliminate(values)
        # Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle
    values = reduce_puzzle(values)
    if values is False:
        return False  ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values  ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    number_of_options, unfilled_box = min((len(values[box]), box) for box in boxes if len(values[box]) > 1)
    # Use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for value in values[unfilled_box]:
        new_sudoku = values.copy()
        new_sudoku[unfilled_box] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    # values = {}
    # for box, value in grid_values(grid).items():
    #     print(box,value)
    #     values = assign_value(values,box,value)
    values = grid_values(grid)
    return search(values)


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments

        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
