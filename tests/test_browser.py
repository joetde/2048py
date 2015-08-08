
from engine.browser import Browser, Keys
# from pyvirtualdisplay import Display

def test_read_grid():
  # display = Display(visible=0)
  # display.start()
  browser = Browser()
  grid = browser.read_grid()
  browser.close()
  nb_zero = sum([row.count(0) for row in grid])
  assert nb_zero == 14

def test_press_key_up():
  browser = Browser()
  browser.press_key(Keys.UP)
  grid = browser.read_grid()
  browser.close()
  nb_zero_top = grid[0].count(0)
  nb_zero_rest = sum([row.count(0) for row in grid[1:]])
  assert nb_zero_top == 2 or nb_zero_top == 1
  assert nb_zero_rest == 11 or nb_zero_rest == 12

def test_press_key_down():
  browser = Browser()
  browser.press_key(Keys.DOWN)
  grid = browser.read_grid()
  browser.close()
  nb_zero_bottom = grid[-1].count(0)
  nb_zero_rest = sum([row.count(0) for row in grid[:-1]])
  assert nb_zero_bottom == 2 or nb_zero_bottom == 1
  assert nb_zero_rest == 11 or nb_zero_rest == 12
