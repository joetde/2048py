#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='2048py',
      version='0.1',
      description='Bot to play 2048 game',
      author='joetde',
      url='https://github.com/joetde/2048py',
      scripts=['src/2048.py'],
      packages=find_packages('src'),
      package_dir = {'':'src'},
      install_requires=['retrying>=1.0', 'selenium>=2.47', 'timeout-decorator>=0.3'],
      )
