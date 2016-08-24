
from random import choice

from lib2048.solve.simulator import POSSIBLE_MOVES
from lib2048.solve.solver import Solver


class RandomSolver(Solver):
    def solve(self, _):
        return choice(POSSIBLE_MOVES)
