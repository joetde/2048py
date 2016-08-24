from __future__ import division

from itertools import imap
from math import log
from timeout_decorator import timeout

from lib2048.helpers.metrics import with_time, with_count
from lib2048.solve.simulator import get_possible_grids, simulate_move, create_new_grid_with_move, Keys, get_at

_KEYS = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

class Solver(object):
    pass

# heuristics for scoring leaves
min_cell = lambda g: sum([r.count(0) for r in g])


@with_count(2 * 4 * 4)
def custer_weigh(grid):
    ''' Gives higher score to clusters of close scores '''
    score = 0
    for key in [Keys.UP, Keys.RIGHT]:
        for ii in range(len(grid) - 1):
            for jj in range(len(grid) - 1):
                curr = get_at(ii, jj, grid, key)
                right = get_at(ii + 1, jj, grid, key)
                down = get_at(ii, jj + 1, grid, key)
                score += _closeness(curr, right)
                score += _closeness(curr, down)
    score += 8 * min_cell(grid)
    return score


def _closeness(curr, neighbour):
    if curr == 0 or neighbour == 0:
        return 0
    if curr == neighbour or curr == neighbour * 2 or curr * 2 == neighbour:
        return max(_weigh_log(curr), _weigh_log(neighbour))
    else:
        return -abs(_weigh_log(curr) - _weigh_log(neighbour))


def _weigh_log(x):
    return log(x, 2)


# heuristics recursive weight
only_min_weight = min
average = lambda l: sum(l) / len(l)


@timeout(5)
@with_time
def solve(grid, eval_leaf=custer_weigh, eval_rec=average, max_depth=4, max_child=4):
    ''' Returns the best move for a given grid.
    eval_leaf: evaluation function for leaves
    eval_rec : evaluation function for recursive calls
    max_depth: how many moves to simulate
    max_child: n first child nodes (most probable first) for each simultation '''
    return _solve_rec_boot(grid, eval_leaf, eval_rec, max_depth, max_child, 0)[0]


def _solve_rec_boot(grid, eval_leaf, eval_rec, max_depth, max_child, curr_depth):
    scores = []
    for key in _KEYS:
        new_grid = create_new_grid_with_move(grid, key)
        if new_grid == grid:
            continue
        _, score = _solve_rec(new_grid, eval_leaf, eval_rec, max_depth, max_child, curr_depth + 1)
        scores.append((key, score))
    if not scores:
        raise Exception("Game Over")
    return max(scores, key=lambda (_, s): s)


@with_count(1)
def _solve_rec(grid, eval_leaf, eval_rec, max_depth, max_child, curr_depth):
    if curr_depth == max_depth:
        return (None, eval_leaf(grid))
    scores = []
    for key in _KEYS:
        grids = sorted(get_possible_grids(grid, key), key=lambda (_, p): -p)[:max_child]
        for grid, _ in grids:
            simulate_move(grid, key)
        grids = [(g, p) for g, p in grids if g != grid]
        if not grids:
            continue
        evals = list(
            imap(lambda (g, _): _solve_rec(g, eval_leaf, eval_rec, max_depth, max_child, curr_depth + 1), grids))
        score = eval_rec([e for _, e in evals])
        scores.append((key, score))
    if not scores:
        return (None, -1)
    return max(scores, key=lambda (_, s): s)
