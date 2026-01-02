# pylint: disable=missing-docstring


def sudoku_validator(grid):
    valid_set = set(range(1, 10))


    # check rows
    for row in grid:
        if set(row) != valid_set:
            return False

    # check columns
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if set(column) != valid_set:
            return False

    # check 3x3 sub-grids
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = []
            for r in range(3):
                for c in range(3):
                    box.append(grid[box_row + r][box_col + c])
            if set(box) != valid_set:
                return False

    return True