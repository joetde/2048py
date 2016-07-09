from copy import deepcopy

# not the best here, but since selenium defines them...
from engine.browser import Keys


def create_new_grid_with_move(grid, key):
    """ Create a new grid from the given grid, with the given action simulated. """
    new_grid = deepcopy(grid)
    simulate_move(new_grid, key)
    return new_grid


def simulate_move(grid, key):
    """ Simulate movement on the given grid. """
    for ii in range(len(grid)):
        last = get_at(ii, 0, grid, key)
        last_pos = 0
        for jj in range(1, len(grid)):
            curr = get_at(ii, jj, grid, key)
            if curr == 0:
                pass
            elif curr == last:
                set_at(ii, jj, 0, grid, key)
                set_at(ii, last_pos, 2 * curr, grid, key)
                last = 2 * curr
            else:
                set_at(ii, jj, 0, grid, key)
                last_pos += 1 if last != 0 else 0
                set_at(ii, last_pos, curr, grid, key)
                last = curr


def get_rotated_coordinates(ii, jj, key, size):
    """ Helper to abstract rotation. """
    if key == Keys.LEFT:
        return ii, jj
    elif key == Keys.RIGHT:
        return ii, size - 1 - jj
    elif key == Keys.UP:
        return jj, size - 1 - ii
    elif key == Keys.DOWN:
        return size - 1 - jj, ii
    raise Exception("Unknown key %s, this shouldn't happen!" % key)


def get_at(ii, jj, grid, key):
    i, j = get_rotated_coordinates(ii, jj, key, len(grid))
    return grid[i][j]


def set_at(ii, jj, value, grid, key):
    i, j = get_rotated_coordinates(ii, jj, key, len(grid))
    grid[i][j] = value


def get_possible_grids(grid, key):
    """ Create the list of all possible grids from a given grid and move.
    Returns list of grids and their probability. [(grid, probability)]"""
    issues = float(sum([row.count(0) for row in grid]))
    positions = []
    for ii in range(len(grid)):
        last_zero = -1
        zero_count = 0.
        for jj in range(0, len(grid)):
            curr = get_at(ii, jj, grid, key)
            if curr == 0:
                zero_count += 1
                last_zero = jj
            else:
                if zero_count != 0:
                    positions.append((ii, last_zero, zero_count / issues))
                    zero_count = 0
        if zero_count != 0:
            positions.append((ii, last_zero, zero_count / issues))
    grids = []
    for ii, jj, prob in positions:
        new_grid = deepcopy(grid)
        # note, 4 is also possible need update for better prevision
        set_at(ii, jj, 2, new_grid, key)
        grids.append((new_grid, prob))
    return grids
