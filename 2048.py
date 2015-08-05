#!/usr/bin/env python

# Full builtin imports
import re

# Partial builtin imports
from argparse import ArgumentParser
from copy import deepcopy

# Partial dependency imports
from selenium import webdriver

g_driver = None
g_game_url = "http://gabrielecirulli.github.io/2048/"
g_empty_grid = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

def static_init():
  ''' Initialization of globals. '''
  global g_driver
  g_driver = webdriver.Chrome()
  g_driver.get(g_game_url)

def static_fini():
  g_driver.close()

def read_grid():
  ''' Returns 2048 grid. Requires driver initialized and open on the game's page. '''
  tiles = g_driver.find_elements_by_tag_name('div')
  tiles = filter(lambda t : 'tile-position' in t.get_attribute('class'), tiles)
  grid = deepcopy(g_empty_grid)
  for tile in tiles:
  	j,i = get_position_from_class(tile)
  	val = int(tile.text)
  	grid[i-1][j-1] = val
  print grid
  return grid

def get_position_from_class(tile):
  ''' Get the position from div object, with its class name. '''
  class_name = tile.get_attribute('class')
  matches = re.search('tile-position-(\d)-(\d)', class_name)
  return int(matches.group(1)), int(matches.group(2))

if __name__ == '__main__':
  parser = ArgumentParser(description='Tired of playing 2048? Let your computer do it for you!')
  args = parser.parse_args()

  static_init()
  read_grid()
  static_fini()