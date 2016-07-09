from nose.tools import assert_not_equal

from engine import solve, Keys, average


def test_solve_forbiden_actions():
    key = solve([[2, 2, 4, 16],
                 [0, 0, 8, 4],
                 [0, 0, 0, 2],
                 [0, 0, 0, 4]])
    assert_not_equal(key, Keys.UP)


def test_solve_blocked():
    key = solve([[2, 16, 4, 8],
                 [8, 8, 32, 256],
                 [4, 32, 4, 4],
                 [0, 2, 0, 8]], eval_rec=average)
    assert_not_equal(key, Keys.UP)
