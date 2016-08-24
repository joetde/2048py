from nose.tools import assert_equals

from lib2048.engine.browser import Browser, Keys
from lib2048.solve.simulator import create_new_grid_with_move


def assert_at_most_one_different_element(grid_ref, grid):
    assert_equals(len(grid_ref), len(grid))
    count_diff = 0
    for i in range(len(grid_ref)):
        assert_equals(len(grid_ref[i]), len(grid[i]))
        for j in range(len(grid_ref[i])):
            if grid_ref[i][j] != grid[i][j]:
                count_diff += 1
    assert count_diff <= 1


def test_read_grid():
    # display = Display(visible=0)
    # display.start()
    browser = Browser()
    grid = browser.read_grid()
    browser.close()
    nb_zero = sum([row.count(0) for row in grid])
    assert_equals(nb_zero, 14)


def test_press_key_up():
    browser = Browser()
    grid_orig = browser.read_grid()
    browser.press_key(Keys.UP)
    grid = browser.read_grid()
    browser.close()
    grid_ref = create_new_grid_with_move(grid_orig, Keys.UP)
    assert_at_most_one_different_element(grid_ref, grid)


def test_press_key_down():
    browser = Browser()
    grid_orig = browser.read_grid()
    browser.press_key(Keys.DOWN)
    grid = browser.read_grid()
    browser.close()
    grid_ref = create_new_grid_with_move(grid_orig, Keys.DOWN)
    assert_at_most_one_different_element(grid_ref, grid)
