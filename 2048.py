#!/usr/bin/env python

from argparse import ArgumentParser
from copy import deepcopy

from engine.browser import Browser, Keys
from helpers.print_util import print_matrix

def get_new_grid_with_movement(grid, key):
  ''' Create a new grid from the given grid, with the action simulated. '''
  new_grid = deepcopy(grid)
  simulate_movement(new_grid, key)
  return new_grid

def simulate_movement(grid, key):
  ''' Simulate movement on the given grid. '''
  for ii in range(len(grid)):
  	for jj in range(len(grid)):
  		i,j = get_rotated_coordinates(ii, jj, key)

def get_all_possible_grids(grid, next_key):
  ''' Create the list of all possible grids from a given grid. '''
  pass

if __name__ == '__main__':
  parser = ArgumentParser(description='Tired of playing 2048? Let your computer do it for you!')
  parser.add_argument('-b', '--browser', dest='browser', type=str, help='Browser to use for the simulation.')
  args = parser.parse_args()

  browser = Browser(args.browser)
  print_matrix(browser.read_grid())
  browser.press_key(Keys.DOWN)
  print_matrix(browser.read_grid())
  browser.close()
