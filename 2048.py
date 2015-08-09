#!/usr/bin/env python

from argparse import ArgumentParser

from engine.browser import Browser, Keys
from helpers.print_util import print_matrix

if __name__ == '__main__':
  parser = ArgumentParser(description='Tired of playing 2048? Let your computer do it for you!')
  parser.add_argument('-b', '--browser', dest='browser', type=str, help='Browser to use for the simulation.')
  args = parser.parse_args()

  browser = Browser(args.browser)
  print_matrix(browser.read_grid())
  browser.press_key(Keys.DOWN)
  print_matrix(browser.read_grid())
  browser.close()
