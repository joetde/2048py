from nose.tools import assert_not_equal

from lib2048.solve.heuristic import avg
from lib2048.solve.heuristic_solver import HeuristicSolver
from lib2048.solve.simulator import Keys

def test_solve_forbiden_actions():
    solver = HeuristicSolver()
    key = solver.solve([[2, 2, 4, 16],
                        [0, 0, 8, 4],
                        [0, 0, 0, 2],
                        [0, 0, 0, 4]])
    assert_not_equal(key, Keys.UP)


def test_solve_blocked():
    solver = HeuristicSolver()
    key = solver.solve([[2, 16, 4, 8],
                        [8, 8, 32, 256],
                        [4, 32, 4, 4],
                        [0, 2, 0, 8]],
                       eval_rec=avg)
    assert_not_equal(key, Keys.UP)
