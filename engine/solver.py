
from itertools import imap

from timeout_decorator import timeout

from helpers.metrics import with_time
from engine.simulator import get_possible_grids, simulate_move, create_new_grid_with_move, Keys

_KEYS = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]
_DEF_LEAF = lambda g : sum([r.count(0) for r in g])
_DEF_REC  = min

@timeout(5)
@with_time
def solve(grid, eval_leaf = _DEF_LEAF, eval_rec = _DEF_REC, max_depth = 4, max_child = 4):
  ''' Returns the best move for a given grid.
  eval_leaf: evaluation function for leaves
  eval_rec : evaluation function for recursive calls
  max_depth: how many moves to simulate
  max_child: n first child nodes (most probable first) for each simultation '''
  return _solve_rec_boot(grid, eval_leaf, eval_rec, max_depth, max_child, 0)

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
  return max(scores, key = lambda (_,s) : s)

def _solve_rec(grid, eval_leaf, eval_rec, max_depth, max_child, curr_depth):
  if curr_depth == max_depth:
    return (None, eval_leaf(grid))
  scores = []
  for key in _KEYS:
    grids = sorted(get_possible_grids(grid, key), key = lambda (_,p) : -p)[:max_child]
    for grid,_ in grids:
      simulate_move(grid, key)
    grids = [(g,p) for g,p in grids if g != grid]
    if not grids:
      continue
    evals = list(imap(lambda (g,_) : _solve_rec(g, eval_leaf, eval_rec, max_depth, max_child, curr_depth + 1), grids))
    score = eval_rec([e for _,e in evals])
    scores.append((key, score))
  if not scores:
    return (None, -1)
  return max(scores, key = lambda (_,s) : s)
