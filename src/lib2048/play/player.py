
from lib2048.browse.browser import Browser
from lib2048.helpers.print_util import print_matrix
from lib2048.solve.solver import Solver, solve


class Player(object):

    def __init__(self, browser_name):
        self._browser = Browser(browser_name)
        self._solver = Solver()

    def play(self):
        playing = True

        while playing:
            grid = self._browser.read_grid()
            score = self._browser.read_score()
            free_cells = sum([r.count(0) for r in grid])

            print score
            print_matrix(grid)

            if free_cells == 0:
                playing = False
            else:
                self._browser.press_key(solve(grid)[0])

        self._browser.close()