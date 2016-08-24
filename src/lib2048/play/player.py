
from lib2048.generic.print_util import print_matrix
from lib2048.solve.simulator import is_game_over


class Player(object):

    def __init__(self, game, solver):
        self._game = game
        self._solver = solver

    def play(self):
        playing = True

        while playing:
            grid = self._game.read_grid()
            score = self._game.read_score()

            print score
            print_matrix(grid)

            if is_game_over(grid):
                playing = False
            else:
                best_move = self._solver.solve(grid)[0]
                self._game.press_key(best_move)

        self._game.finish()