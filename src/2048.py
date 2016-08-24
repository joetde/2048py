#!/usr/bin/env python

from argparse import ArgumentParser

from lib2048.play.player import Player

if __name__ == '__main__':
    parser = ArgumentParser(description='Tired of playing 2048? Let your computer do it for you!')
    parser.add_argument('-b', '--browser', dest='browser', type=str, help='Browser to use for the simulation.', default='phantomjs')
    args = parser.parse_args()

    player = Player(args.browser)
    player.play()
