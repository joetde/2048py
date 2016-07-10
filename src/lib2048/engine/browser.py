import re
from copy import deepcopy

from selenium import webdriver
# pylint: disable=unused-import
from selenium.webdriver.common.keys import Keys
from retrying import retry

from lib2048.helpers.metrics import with_time

# Deactivate DEBUG logging for selenium
import logging
selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
selenium_logger.setLevel(logging.WARNING)


def _get_position_from_class(tile):
    """ Get the position from div object, with its class name. """
    class_name = tile.get_attribute('class')
    matches = re.search(r'tile-position-(\d)-(\d)', class_name)
    return int(matches.group(1)), int(matches.group(2))


class Browser(object):
    _GAME_URL = "http://gabrielecirulli.github.io/2048/"
    _EMPTY_GRID = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]

    @with_time
    def __init__(self, browser_name="phantomjs"):
        if browser_name == "phantomjs":
            self._driver = webdriver.PhantomJS()
        elif browser_name == "chrome":
            self._driver = webdriver.Chrome()
        elif browser_name == "firefox":
            self._driver = webdriver.Firefox()
        else:
            raise Exception("Unsupported browser: %s" % browser_name)
        self._driver.get(Browser._GAME_URL)
        self._driver.find_element_by_class_name("restart-button").click()
        self._body = self._driver.find_element_by_tag_name('body')

    @retry(stop_max_attempt_number=3)
    @with_time
    def read_grid(self):
        """ Returns 2048 grid. """
        tiles = self._driver.find_elements_by_tag_name('div')
        tiles = [t for t in tiles if 'tile-position' in t.get_attribute('class')]
        grid = deepcopy(Browser._EMPTY_GRID)
        for tile in tiles:
            j, i = _get_position_from_class(tile)
            val = int(tile.text)
            grid[i - 1][j - 1] = val
        return grid

    def read_score(self):
        """ Returns current score. """
        return int(self._driver.find_element_by_class_name("score-container").text)

    @with_time
    def press_key(self, key):
        """ Simulate keypress for the browser. """
        self._body.send_keys(key)

    @with_time
    def close(self):
        self._driver.close()
