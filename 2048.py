#!/usr/bin/env python

# Full builtin imports
import re
import logging

# Partial builtin imports
from argparse import ArgumentParser
from copy import deepcopy
from time import time

# Partial dependency imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

g_driver = None
g_body = None
g_game_url = "http://gabrielecirulli.github.io/2048/"
g_empty_grid = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
g_logger = logging.getLogger('2048.py')
ch = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s:%(asctime)s] %(message)s')
ch.setFormatter(formatter)
g_logger.addHandler(ch)
g_logger.setLevel(logging.DEBUG)

def with_time(func):
  ''' Helper decorator for timing function. '''
  def wrapper(*args, **kwargs):
    start = time() * 1000
    ret = func(*args, **kwargs)
    end = time() * 1000
    time_spent = int(end - start)
    g_logger.debug('<%s> Time spent: %sms' % (func.__name__, time_spent))
    return ret
  return wrapper

def print_matrix(matrix):
  ''' Helper for 2d matrix pretty print. '''
  for row in matrix:
  	for cell in row:
  	  print cell,
  	print

@with_time
def static_init():
  ''' Initialization of globals. '''
  global g_driver
  global g_body
  g_driver = webdriver.Chrome()
  g_driver.get(g_game_url)
  g_body = g_driver.find_element_by_tag_name('body')

@with_time
def static_fini():
  g_driver.close()

@with_time
def read_grid():
  ''' Returns 2048 grid. Requires driver initialized and open on the game's page. '''
  tiles = g_driver.find_elements_by_tag_name('div')
  tiles = filter(lambda t : 'tile-position' in t.get_attribute('class'), tiles)
  grid = deepcopy(g_empty_grid)
  for tile in tiles:
  	j,i = get_position_from_class(tile)
  	val = int(tile.text)
  	grid[i-1][j-1] = val
  return grid

def get_position_from_class(tile):
  ''' Get the position from div object, with its class name. '''
  class_name = tile.get_attribute('class')
  matches = re.search('tile-position-(\d)-(\d)', class_name)
  return int(matches.group(1)), int(matches.group(2))

@with_time
def press_key(key):
  ''' Simulate keypress for the browser. '''
  g_body.send_keys(key)

if __name__ == '__main__':
  parser = ArgumentParser(description='Tired of playing 2048? Let your computer do it for you!')
  args = parser.parse_args()

  static_init()
  print_matrix(read_grid())
  press_key(Keys.DOWN)
  print_matrix(read_grid())
  static_fini()