
from nose.tools import assert_equals, assert_in

from helpers.print_util import print_matrix
from engine.simulator import create_new_grid_with_move, get_rotated_coordinates, get_possible_grids, Keys

test_data_move_down_inp = [[[2,0,0,0],
                            [0,0,0,0],
                            [0,0,0,0],
                            [0,0,0,0]],
                           [[2,4,8,16],
                            [0,0,0,0],
                            [0,0,0,0],
                            [0,0,0,0]],
                           [[0,0,0,0],
                            [0,0,0,0],
                            [0,0,0,0],
                            [0,2,0,0]],
                           [[0,0,0,0],
                            [0,0,2,0],
                            [0,0,0,0],
                            [0,0,4,0]],
                           [[0,0,0,2],
                            [0,0,0,0],
                            [0,0,0,4],
                            [0,0,0,0]],
                           [[2,0,0,0],
                            [2,0,0,0],
                            [4,0,0,0],
                            [4,0,0,0]],
                           [[0,2,0,0],
                            [0,0,0,0],
                            [0,2,0,0],
                            [0,0,0,0]],
                           [[0,0,2,0],
                            [0,0,4,0],
                            [0,0,2,0],
                            [0,0,0,0]]]
test_data_move_down_out = [[[0,0,0,0],
                            [0,0,0,0],
                            [0,0,0,0],
                            [2,0,0,0]],
                           [[0,0,0,0],
                            [0,0,0,0],
                            [0,0,0,0],
                            [2,4,8,16]],
                           [[0,0,0,0],
                            [0,0,0,0],
                            [0,0,0,0],
                            [0,2,0,0]],
                           [[0,0,0,0],
                            [0,0,0,0],
                            [0,0,2,0],
                            [0,0,4,0]],
                           [[0,0,0,0],
                            [0,0,0,0],
                            [0,0,0,2],
                            [0,0,0,4]],
                           [[0,0,0,0],
                            [0,0,0,0],
                            [4,0,0,0],
                            [8,0,0,0]],
                           [[0,0,0,0],
                            [0,0,0,0],
                            [0,0,0,0],
                            [0,4,0,0]],
                           [[0,0,0,0],
                            [0,0,2,0],
                            [0,0,4,0],
                            [0,0,2,0]]]

def rotate(grid, times):
  curr_grid = grid
  for i in range(times):
    curr_grid = zip(*curr_grid[::-1])
  # zip returns tuples...
  curr_grid = [list(row) for row in curr_grid]
  return curr_grid

def test_move_down():
  for i in range(len(test_data_move_down_inp)):
    curr_input = test_data_move_down_inp[i]
    curr_exp_output = test_data_move_down_out[i]
    output = create_new_grid_with_move(curr_input, Keys.DOWN)
    assert_equals(output, curr_exp_output)
    new_output = create_new_grid_with_move(curr_input, Keys.DOWN)
    assert_equals(new_output, output)

def test_move_left():
  for i in range(len(test_data_move_down_inp)):
    curr_input = rotate(test_data_move_down_inp[i], 1)
    curr_exp_output = rotate(test_data_move_down_out[i], 1)
    output = create_new_grid_with_move(curr_input, Keys.LEFT)
    assert_equals(output, curr_exp_output)
    new_output = create_new_grid_with_move(curr_input, Keys.LEFT)
    assert_equals(new_output, output)

def test_move_up():
  for i in range(len(test_data_move_down_inp)):
    curr_input = rotate(test_data_move_down_inp[i], 2)
    curr_exp_output = rotate(test_data_move_down_out[i], 2)
    output = create_new_grid_with_move(curr_input, Keys.UP)
    assert_equals(output, curr_exp_output)
    new_output = create_new_grid_with_move(curr_input, Keys.UP)
    assert_equals(new_output, output)

def test_move_up():
  for i in range(len(test_data_move_down_inp)):
    curr_input = rotate(test_data_move_down_inp[i], 3)
    curr_exp_output = rotate(test_data_move_down_out[i], 3)
    output = create_new_grid_with_move(curr_input, Keys.RIGHT)
    assert_equals(output, curr_exp_output)
    new_output = create_new_grid_with_move(curr_input, Keys.RIGHT)
    assert_equals(new_output, output)

def test_get_rotated_coordinates():
  assert_equals(get_rotated_coordinates(1 , 2, Keys.UP, 4), (2,2))
  assert_equals(get_rotated_coordinates(1 , 2, Keys.RIGHT, 4), (1,1))
  assert_equals(get_rotated_coordinates(1 , 2, Keys.DOWN, 4), (1,1))
  assert_equals(get_rotated_coordinates(1 , 2, Keys.LEFT, 4), (1,2))
  assert_equals(get_rotated_coordinates(1 , 3, Keys.UP, 4), (3,2))
  assert_equals(get_rotated_coordinates(1 , 3, Keys.RIGHT, 4), (1,0))
  assert_equals(get_rotated_coordinates(1 , 3, Keys.DOWN, 4), (0,1))
  assert_equals(get_rotated_coordinates(1 , 3, Keys.LEFT, 4), (1,3))

def test_get_possible_grids():
  grids = get_possible_grids([[0,2,0,2],
                              [0,0,2,2],
                              [0,2,2,0],
                              [0,0,0,0]], Keys.LEFT)
  assert_in(([[2,2,0,2],
              [0,0,2,2],
              [0,2,2,0],
              [0,0,0,0]], 0.1), grids)
  assert_in(([[0,2,2,2],
              [0,0,2,2],
              [0,2,2,0],
              [0,0,0,0]], 0.1), grids)
  assert_in(([[0,2,0,2],
              [0,2,2,2],
              [0,2,2,0],
              [0,0,0,0]], 0.2), grids)
  assert_in(([[0,2,0,2],
              [0,0,2,2],
              [2,2,2,0],
              [0,0,0,0]], 0.1), grids)
  assert_in(([[0,2,0,2],
              [0,0,2,2],
              [0,2,2,2],
              [0,0,0,0]], 0.1), grids)
  assert_in(([[0,2,0,2],
              [0,0,2,2],
              [0,2,2,0],
              [0,0,0,2]], 0.4), grids)
