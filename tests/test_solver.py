
from engine.solver import solve, Keys

def test_solve_forbiden_actions():
  (key,_) = solve([[2,2,4,16],
                   [0,0,8,4],
                   [0,0,0,2],
                   [0,0,0,4]])
  assert key != Keys.UP

def test_solve_blocked():
  (key,_) = solve([[2,16,4,8],
                   [8,8,32,256],
                   [4,32,4,4],
                   [0,2,0,8]])
  assert key != Keys.UP
